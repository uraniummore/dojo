class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        for index, letter in enumerate(s):
            next_letter = s[index + 1] if index < len(s) - 1 else None
            prev_letter = s[index - 1] if index > 0 else None


            if letter == "I":
                if next_letter == "V":
                    result += 4
                elif next_letter == "X":
                    result += 9
                else:
                    result += 1
            if letter == "V":
                if prev_letter != "I":
                    result += 5
            if letter == "X":
                if next_letter == "C":
                    result += 90
                elif prev_letter != "I" and next_letter != "L":
                    result += 10
                elif next_letter == "L":
                    result += 40
            if letter == "L":
                if prev_letter != "X":
                    result += 50
            if letter == "C":
                if next_letter == "M":
                    result += 900
                elif prev_letter != "X" and next_letter != "D":
                    result += 100
                elif next_letter == "D":
                    result += 400
            if letter == "D":
                if prev_letter != "C":
                    result += 500
            if letter == "M":
                if prev_letter != "C":
                    result += 1000

        return result
