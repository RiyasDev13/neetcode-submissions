class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = ""

        for i in range(n):
            for j in range(i+1,n+1):
                substring = s[i:j]
                if substring == substring[::-1] and len(substring) > len(longest):
                    longest = substring
        return longest
        