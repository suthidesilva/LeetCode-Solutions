class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with a dummy index
        max_length = 0
         
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()  # Pop the top index
                
                if not stack:  # If stack becomes empty, push current index as a new starting point
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])  # Update max_length
        
        return max_length
