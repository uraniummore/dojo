from typing import List


class Solution:
    def _check_next_num(self, nums: List[int], current_index: int, num: int):
        if current_index < len(nums) - 1:
            next_num = nums[current_index + 1]
            if next_num == num:
                del nums[current_index + 1]
                self._check_next_num(nums, current_index, num)

    def removeDuplicates(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            self._check_next_num(nums, current_index=index, num=num)

        return len(nums)

a = []

print(Solution().removeDuplicates(a))
