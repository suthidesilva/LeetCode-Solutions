class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            mask = 1 << int(num)
            if rows[row] & mask or cols[col] & mask or subgrids[row // 3][col // 3] & mask:
                return False
            return True
        
        def set_number(row, col, num):
            mask = 1 << int(num)
            rows[row] |= mask
            cols[col] |= mask
            subgrids[row // 3][col // 3] |= mask
        
        def unset_number(row, col, num):
            mask = ~(1 << int(num))
            rows[row] &= mask
            cols[col] &= mask
            subgrids[row // 3][col // 3] &= mask
        
        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(i, j, num):
                                board[i][j] = num
                                set_number(i, j, num)
                                if backtrack():
                                    return True
                                board[i][j] = '.'
                                unset_number(i, j, num)
                        return False
            return True
        
        rows = [0] * 9
        cols = [0] * 9
        subgrids = [[0] * 3 for _ in range(3)]
        
        # Initialize bitmasks for existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    set_number(i, j, board[i][j])
        
        backtrack()
