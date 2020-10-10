from typing import List


class Solution:
    def _calculate(self, nums: List[int]) -> List[int]:
        result = current_sum = prev_sum = 0

        for index, number in enumerate(nums):
            current_sum += number
            if current_sum == 0:
                nums = nums[index:]
                current_sum = self._calculate(nums)
            if current_sum > prev_sum:
                result = prev_sum = current_sum
            if index + 1 == len(nums):
                break

        return result

    def maxSubArray(self, nums: List[int]) -> int:
        return self._calculate(nums)


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
