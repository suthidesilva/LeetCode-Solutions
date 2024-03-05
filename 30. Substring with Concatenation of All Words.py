class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if not s or not words or not words[0]:
            return res
        len_word = len(words[0])
        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1
        for i in range(len_word):
            start = i
            count = 0
            seen = {}
            for j in range(i, len(s) - len_word + 1, len_word):
                sub_s = s[j:j+len_word]
                if sub_s in word_map:
                    seen[sub_s] = seen.get(sub_s, 0) + 1
                    if seen[sub_s] <= word_map[sub_s]:
                        count += 1
                    while count == len(words):
                        start_s = s[start:start+len_word]
                        if seen[start_s] <= word_map[start_s]:
                            count -= 1
                        seen[start_s] -= 1
                        if j - start == len_word * (len(words) - 1):
                            res.append(start)
                        start += len_word
                else:
                    seen.clear()
                    count = 0
                    start = j + len_word
        return res
