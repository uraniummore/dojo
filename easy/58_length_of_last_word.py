class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not len(s.strip()):
            return 0
        array = [word for word in s.split(" ") if word != ""]
        return len(array[-1])

if __name__ == '__main__':
    print(Solution().lengthOfLastWord(" "))
