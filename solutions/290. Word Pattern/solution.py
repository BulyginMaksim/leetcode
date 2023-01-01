class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        current_word = []
        seen_words = dict()
        seen_patterns = dict()
        idx = 0
        for char in s:
            if char != ' ':
                current_word.append(char)
                continue
            word = ''.join(current_word)
            pattern_char = pattern[idx]
            idx += 1
            current_word = []
            if word not in seen_words:
                seen_words[word] = pattern_char
            if pattern_char not in seen_patterns:
                seen_patterns[pattern_char] = word
            is_continue = self.is_fine_bijection(idx, seen_words, seen_patterns, word, pattern)
            if not is_continue:
                return False
        word = ''.join(current_word)
        pattern_char = pattern[idx]
        if word not in seen_words:
            seen_words[word] = pattern_char
        if pattern_char not in seen_patterns:
            seen_patterns[pattern_char] = word
        return self.is_fine_bijection(idx, seen_words, seen_patterns, word, pattern, is_algorithm_end=True)

    def is_fine_bijection(self, idx: int, seen_words: dict, seen_patterns: dict, word: str,
                          pattern: str, is_algorithm_end: bool = False) -> bool:
        if is_algorithm_end:
            idx += 1
        is_good_word = seen_words[word] == pattern[idx - 1]
        is_good_pattern = seen_patterns[pattern[idx - 1]] == word
        is_good_idx = idx == len(pattern) if is_algorithm_end else idx < len(pattern)
        return is_good_word and is_good_pattern and is_good_idx
