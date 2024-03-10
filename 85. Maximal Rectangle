class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n = len(matrix[0])
        height = [0] * (n + 1)  # Add an extra zero to handle the last element in the row

        for row in matrix:
            for i in range(n):
                # Update the height of this histogram
                height[i] = height[i] + 1 if row[i] == '1' else 0

            # Now, calculate the maximum area of the rectangle in this histogram
            stack = [-1]  # Start with a dummy index
            for i in range(n + 1):
                # Maintain a stack of indices with increasing heights
                while height[i] < height[stack[-1]]:  # Need to pop the stack
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1  # Width is the distance between the current index and the one on the stack
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
