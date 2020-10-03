# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [kid_candies + extraCandies >= max(candies) for kid_candies in candies]
