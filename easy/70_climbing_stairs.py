import math


class Solution:
    def climbStairs(self, num: int) -> int:
        result = 0

        max_twos = self._find_max_twos(num)

        while max_twos >= 0:
            sum_from_twos = max_twos * 2
            possible_ones = num - sum_from_twos

            result += self._find_possible_combinations(possible_ones, max_twos)

            max_twos = max_twos - 1

        return result

    def _find_max_twos(self, num: int) -> int:
        remainder = num % 2
        return math.floor((num - remainder) / 2)

    def _find_possible_combinations(self, ones_count: int, twos_count: int) -> int:
        possible_permutations = math.factorial(ones_count + twos_count)
        number_to_divide = math.factorial(ones_count) * math.factorial(twos_count)

        return int(possible_permutations / number_to_divide)


if __name__ == '__main__':
    print(Solution().climbStairs(31))
