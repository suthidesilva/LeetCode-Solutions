class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        max_length = 0
        start = 0
        seen = {}

        for end, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                max_length = max(max_length, end - start + 1)

            seen[char] = end

        return max_length
