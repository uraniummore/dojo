class Solution:
    opening_parentheses = {"(": "round", "[": "square", "{": "curly"}
    closing_parentheses = {")": "round", "]": "square", "}": "curly"}

    def isValid(self, s: str) -> bool:
        opened_parentheses = tuple()

        for symbol in s:
            if symbol in self.opening_parentheses.keys():
                opened_parentheses += (self.opening_parentheses[symbol],)
            if symbol in self.closing_parentheses.keys():
                if not opened_parentheses:
                    return False
                last_parentheses = opened_parentheses[-1]
                current_parentheses = self.closing_parentheses[symbol]

                if last_parentheses == current_parentheses:
                    opened_parentheses = opened_parentheses[0: -1]
                else:
                    key_index = list(self.closing_parentheses.keys()).index(symbol)
                    invalid_parentheses = list(self.opening_parentheses.keys())[key_index]
                    opened_parentheses += (invalid_parentheses,)

        return not opened_parentheses


print(Solution().isValid("[)]"))
