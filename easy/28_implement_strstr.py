class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if needle not in haystack:
            return -1

        self.result = -1
        original_haystack = haystack
        haystack = self._try_to_find_needle(haystack, needle)

        return len(original_haystack) - len(haystack)

    def _try_to_find_needle(self, haystack: str, needle: str) -> str:
        for index, letter in enumerate(haystack):
            if letter == needle[0]:
                new_haystack = haystack[index:]

                if not new_haystack.startswith(needle):
                    new_haystack = haystack[index + 1:]
                    return self._try_to_find_needle(new_haystack, needle)
                else:
                    return new_haystack

# print(Solution().strStr("hello", "ll"))

# should be 3
if __name__ == '__main__':
    # print(Solution().strStr(
    #     "folfolder",
    #     "folder"
    # ))

    print(Solution().strStr(
        "mississippi",
        "pi"
    ))
