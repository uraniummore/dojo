# Problem URL: https://leetcode.com/problems/running-sum-of-1d-array
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []

        for index, number in enumerate(nums):
            if index > 0:
                number += result[index - 1]
            result.append(number)

        return result
