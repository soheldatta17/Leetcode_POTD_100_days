# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/?envType=daily-question&envId=2024-08-04

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        prefix_sums = [0] * (n + 1)

        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        subarray_sums = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray_sums.append(prefix_sums[j] - prefix_sums[i])

        subarray_sums.sort()

        result = sum(subarray_sums[left-1:right]) % MOD
        
        return result
