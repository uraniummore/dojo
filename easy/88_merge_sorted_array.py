from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for index, item in enumerate(sorted(nums1[0:m] + nums2[0:n])):
            nums1[index] = item


if __name__ == '__main__':
    Solution().merge(
        [-1, 0, 0, 3, 3, 3, 0, 0, 0],
        6,
        [1, 2, 2],
        3
    )
