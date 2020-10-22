from typing import List


class Solution:
    def _delete_number(self, array: List[int], num_to_delete: int) -> List[int]:
        for num in array:
            if num == num_to_delete:
                del array[array.index(num)]
        if num_to_delete in array:
            self._delete_number(array, num_to_delete)

    def removeElement(self, nums: List[int], val: int) -> int:
        self._delete_number(nums, val)

        return len(nums)


a = [0]
print(Solution().removeElement(a, 3))
