class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n_bulls = 0
        first, second = dict(), dict()
        for secret_char, guess_char in zip(secret, guess):
            if secret_char == guess_char:
                n_bulls += 1
                continue
            if secret_char not in first:
                first[secret_char] = 0
            if guess_char not in second:
                second[guess_char] = 0
            first[secret_char] += 1
            second[guess_char] += 1
        n_cows = 0
        for guess_char, frequency in second.items():
            if guess_char not in first:
                continue
            n_cows += min(frequency, first[guess_char])
        return f'{n_bulls}A{n_cows}B'
