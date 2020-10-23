from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for index, num in enumerate(nums):
                if num > target:
                    return index
                if index + 1 == len(nums):
                    return index + 1


if __name__ == '__main__':
    print(Solution().searchInsert(
        [1, 3, 5],
        2
    ))
