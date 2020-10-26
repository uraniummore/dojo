from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit_string = "".join((str(num) for num in digits))
        digit = int(digit_string) + 1
        return [int(letter) for letter in str(digit)]

if __name__ == '__main__':
    print(Solution().plusOne([6, 9, 4, 2, 0]))
    print(Solution().plusOne([0]))
