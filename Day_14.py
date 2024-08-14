# https://leetcode.com/problems/find-k-th-smallest-pair-distance/?envType=daily-question&envId=2024-08-14

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(nums: List[int], mid: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs(nums, mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
