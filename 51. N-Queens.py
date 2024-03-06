class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
        result = []
        DFS([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in sols] for sols in result]
