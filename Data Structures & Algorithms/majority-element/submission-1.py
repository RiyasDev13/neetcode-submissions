from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_var = Counter(nums)
        return max(counter_var,key=counter_var.get)
        