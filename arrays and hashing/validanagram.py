class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {}
        mydictt={}
        if len(s)!=len(t):
            return False 
        for i in range(len(s)):
            mydict[s[i]]= 1 + mydict.get(s[i],0)
            mydictt[t[i]] = 1+ mydictt.get(t[i],0)
        for i in mydict.keys():
            if mydict[i]!=mydictt.get(i,0):
                return False
        return True 