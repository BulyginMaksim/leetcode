class Solution:
    def toLowerCase(self, s: str) -> str:
        result = [char.lower() for char in s]
        return ''.join(result)
