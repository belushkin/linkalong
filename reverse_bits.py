import sys


class Solution:

    # 1 000 000 000
    # 111 011 100 110 101 100 101 000 000 000
    def reverseBits(self, n: int) -> int:
        res = 0
        int_size = self.getIntSize(n)
        for i in range(int_size):
            res += ((n & 1) * 2) ** (int_size - 1 - i)
            if int_size - 1 - i == 0 and n & 1 == 0:
                res -= 1
            n = n >> 1
        return res

    def getIntSize(self, n: int) -> int:
        size = 32
        start = 2147483648
        while start > 0:
            if n & start > 0:
                return size
            start //= 2
            size -= 1

        return 0


solution = Solution()
# print(solution.reverseBits(43261596))  # 964176192(00111001011110000010100101000000)
# print(solution.reverseBits(1))  # 2147483648 (10000000000000000000000000000000)
# print(solution.reverseBits(2))
# print(solution.reverseBits(3))
# print(solution.reverseBits(0))
# print(solution.reverseBits(4294967293))  # 3221225471(10111111111111111111111111111111)
# print(solution.reverseBits(int(sys.argv[1])))


print(solution.reverseBits(int(sys.argv[1])))
