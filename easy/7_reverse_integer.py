# URL: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = "0"
        result = str(x)[::-1]
        if int(result.strip("-")).bit_length() >= 32:
            return 0
        if len(result) > 1:
            result = result.lstrip("0")
        if x < 0:
            result = f"-{result[:-1]}"
        return result
