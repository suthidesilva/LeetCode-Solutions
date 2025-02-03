class Solution:
    def isValid(self, s: str) -> bool:
        s_dic = {'(':')','{':'}','[':']'}
        stack = []

        if len(s) % 2 == 1:
            return False                

        for sym in s:
            if sym in s_dic:
                stack.append(sym)
            elif sym in s_dic.values():
                if not stack or s_dic[stack[-1]] != sym:
                    return False
                stack.pop()
            else:
                return False
        return not stack
                
