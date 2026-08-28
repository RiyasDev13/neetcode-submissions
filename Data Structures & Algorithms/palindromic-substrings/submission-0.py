class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n     = len(s)

        for i in range(n):
            for j in range(i+1,n+1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    count += 1
        return count
        