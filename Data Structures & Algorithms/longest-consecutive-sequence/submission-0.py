class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        res = set(nums)

        for num in nums:
            streak,curr = 0 , num
            while curr in res:
                streak += 1
                curr += 1
            longest = max(longest,streak)
        return longest
        