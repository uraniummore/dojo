from typing import List


class Solution:
    def _find_prefix(self, word_1, word_2) -> str:
        prefix = ""
        last_index = 0
        words_zip = zip(word_1, word_2)

        for index, letters in enumerate(words_zip):
            first_letter, second_letter = letters
            if index - last_index == 1 or last_index == 0:
                if first_letter == second_letter:
                    prefix += first_letter
                else:
                    break
                last_index = index
            else:
                break

        return prefix

    def longestCommonPrefix(self, words: List[str]) -> str:
        longest_prefix = None

        for index, word in enumerate(words):
            second_word = words[index - 1] if longest_prefix is None else longest_prefix
            longest_prefix = self._find_prefix(word, second_word)

        longest_prefix = longest_prefix if longest_prefix else ""

        return longest_prefix
