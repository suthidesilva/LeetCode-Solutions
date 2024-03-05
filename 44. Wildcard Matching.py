class Solution(object):
    def isMatch(self, s, p):
        pLen,sLen = len(p),len(s)
        i = j = 0
        starIndex = stemp = - 1
        while j<sLen:
            if i<pLen and p[i] in ["?",s[j]]:
                i+=1
                j+=1
            
            elif i<pLen and p[i]=="*":
                starIndex = i
                stemp = j
                i+=1
            elif starIndex == -1:
                return False
            
            else:
                i = starIndex +1
                j = stemp + 1
                stemp = j
        return all(p[i] == '*' for i in range(i, pLen))
