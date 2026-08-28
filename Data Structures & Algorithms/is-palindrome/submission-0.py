class Solution:
    def isPalindrome(self, s: str) -> bool:

        result = ""

        for word in s:
            if word.isalpha():
                result += word.lower()
            if word.isnumeric():
                result += word
        return result == result[::-1] 