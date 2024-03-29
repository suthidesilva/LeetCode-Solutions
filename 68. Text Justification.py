class Solution(object):
    def justifyLine(self, line, maxWidth, isLast=False):
        # For the last line or lines with a single word, left-justify
        if isLast or len(line) == 1:
            return " ".join(line).ljust(maxWidth)
        # Calculate total space needed and the number of gaps between words
        spaces = maxWidth - sum(len(word) for word in line)
        gaps = len(line) - 1
        # Calculate even distribution of spaces and the remainder to distribute from left to right
        evenSpaces, remainder = divmod(spaces, gaps)
        # Build the line with even distribution and add remainder spaces to the left gaps
        for i in range(remainder):
            line[i] += ' '
        return (' ' * evenSpaces).join(line)

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result, currentLine, currentLength = [], [], 0
        for word in words:
            # Check if adding the next word exceeds maxWidth
            if currentLength + len(word) + len(currentLine) > maxWidth:
                # Justify the current line and reset for the next line
                result.append(self.justifyLine(currentLine, maxWidth))
                currentLine, currentLength = [], 0
            currentLine.append(word)
            currentLength += len(word)

        # Handle the last line
        result.append(self.justifyLine(currentLine, maxWidth, isLast=True))
        return result
        
