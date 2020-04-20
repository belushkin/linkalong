from typing import List
import sys


class Solution:
    def spiralOrder(self, matrix: List[List[int]]):  # -> List[int]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        size = len(matrix) * len(matrix[0]) if len(matrix) > 0 else 0
        pos = 0
        position = (0, 0)
        # output = []

        for i in range(size):
            y, x = position
            # output.append(matrix[y][x])
            print((y, x))
            matrix[y][x] = sys.maxsize
            if 0 <= x + dirs[pos][1] < len(matrix[0]) and 0 <= y + dirs[pos][0] < len(matrix) and \
                    matrix[y + dirs[pos][0]][x + dirs[pos][1]] != sys.maxsize:
                position = (y + dirs[pos][0], x + dirs[pos][1])
            else:
                pos = pos + 1 if pos + 1 < len(dirs) else 0
                position = (y + dirs[pos][0], x + dirs[pos][1])

        # return output


w, h = sys.argv[1].split('x')
matrix = [[0 for x in range(int(w))] for y in range(int(h))]

solution = Solution()
solution.spiralOrder(matrix)

# print(solution.spiralOrder([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]))

# print(solution.spiralOrder([
#     [1, 2],
#     [4, 5],
#     [7, 8]
# ]))

# print(solution.spiralOrder([
#     [1],
#     [4],
#     [7]
# ]))

# print(solution.spiralOrder([
#     [1, 2, 3],
#     [4, 5, 6]
# ]))

# print(solution.spiralOrder([
#     [1, 2, 3]
# ]))

# print(solution.spiralOrder([
#     [1]
# ]))


# print(solution.spiralOrder([]))
