class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Special cases: negative numbers and numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Initialize reversed number
        reversed_num = 0
        
        # Reverse the second half of x and compare it with the first half
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # If x has an odd number of digits, we can ignore the middle digit by x == reversed_num // 10
        return x == reversed_num or x == reversed_num // 10
