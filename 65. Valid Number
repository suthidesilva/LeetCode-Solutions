class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Flags to indicate if we've seen a digit, an exponent, or a dot.
        seenDigit = seenExponent = seenDot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seenDigit = True
            elif char in ['e', 'E']:
                # If we've already seen an exponent or haven't seen a digit yet, it's invalid.
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False  # Reset for the exponent part
            elif char == '.':
                # If we've already seen a dot or an exponent, it's invalid.
                if seenDot or seenExponent:
                    return False
                seenDot = True
            elif char in ['+', '-']:
                # A sign is valid only at the beginning or just after an exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            else:
                # Invalid character
                return False
        
        return seenDigit  # A valid number must include at least one digit.
