# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        count = nums.count(1)
        n = len(nums)
        if count == 0 or count == n:
            return 0

        current_zero_count = nums[:count].count(0)
        min_zero_count = current_zero_count

        for i in range(1, n):
            if nums[i - 1] == 0:
                current_zero_count -= 1
            if nums[(i + count - 1) % n] == 0:
                current_zero_count += 1

            min_zero_count = min(min_zero_count, current_zero_count)

        return min_zero_count
