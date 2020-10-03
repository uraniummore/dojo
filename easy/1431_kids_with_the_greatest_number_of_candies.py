from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [kid_candies + extraCandies >= max(candies) for kid_candies in candies]
