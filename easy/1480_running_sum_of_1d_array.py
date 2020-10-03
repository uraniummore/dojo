# Problem URL: https://leetcode.com/problems/running-sum-of-1d-array
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [number + sum(nums[0: index]) if index > 0 else number for index, number in enumerate(nums)]
