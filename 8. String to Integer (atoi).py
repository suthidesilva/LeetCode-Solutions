class Solution(object):
    def myAtoi(self, s):
        if not s:
            return 0
        
        i = 0
        n = len(s)
        
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if there is a sign
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Read digits until a non-digit character or end of string is encountered
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if result > (2147483647 - digit) // 10:
                return 2147483647 if sign == 1 else -2147483648
            result = result * 10 + digit
            i += 1
        
        return sign * result
