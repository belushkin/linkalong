class Solution:

    # 1 000 000 000
    # 111 011 100 110 101 100 101 000 000 000
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += ((n & 1) * 2) ** (31 - i)
            if 31 - i == 0 and n & 1 == 0:
                res -= 1
            n = n >> 1
        return res


solution = Solution()
print(solution.reverseBits(43261596))  # 964176192(00111001011110000010100101000000)
print(solution.reverseBits(1))  # 2147483648 (10000000000000000000000000000000)
print(solution.reverseBits(2))
print(solution.reverseBits(3))
print(solution.reverseBits(0))
print(solution.reverseBits(4294967293))  # 3221225471(10111111111111111111111111111111)
