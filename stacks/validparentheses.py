class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {}
        mydict["("] = ")"
        mydict["{"]= "}"
        mydict["["] = "]"

        stack = []
        for i in range(len(s)):
            if s[i] in mydict.keys():
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    check = stack.pop()
                    if mydict[check] != s[i]:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False