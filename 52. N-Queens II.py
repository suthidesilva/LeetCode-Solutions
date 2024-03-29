class Solution(object):
    def totalNQueens(self, n):
        def backtrack(row, columns, diagonals1, diagonals2):
            if row == n:
                return 1
            else:
                count = 0
                available_positions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while available_positions:
                    position = available_positions & -available_positions  # Get the rightmost available position
                    available_positions &= available_positions - 1  # Clear the rightmost set bit
                    count += backtrack(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)
                return count
        
        return backtrack(0, 0, 0, 0)
