class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))

if __name__ == '__main__':
    print(Solution().addBinary("1010", "1011"))
