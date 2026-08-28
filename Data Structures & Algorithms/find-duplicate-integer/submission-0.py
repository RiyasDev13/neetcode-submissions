class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            if nums.count(num) > 1:
                return num

      
        