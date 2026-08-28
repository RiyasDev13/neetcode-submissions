class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        bin_val = bin(n)[2:]
        for num in bin_val:
            if num == '1':
                count += 1
        return count

        