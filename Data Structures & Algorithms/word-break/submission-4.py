class Solution:
    def wordBreak(self,s,words):
        
        word = [True]

        for i in range(1,len(s)+1):
            word += any(word[j] and s[j:i] in words 
                for j in range(i)
            ),
        return word[-1]