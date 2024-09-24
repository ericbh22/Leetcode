class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # #sorting strategy is a lot better
        # res= defaultdict(list)
        # for s in strs:
        #     count = [0] * 26 #resetting this everytime 
        #     for c in s:
        #         count[ord(c) - ord("a")] +=1 #basically creates a map of where every vcalue is everytime 
            
        #     res[tuple(count)].append(s) #lists are non mutable , default list works here 
        # return res.values()

        #find all the anagrams and group thjem together

        #or 

        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s)) # turns list into string, and the list is just the item sorted
            ans[key].append(s) # key = sortedanswer, append the actual unscarambled as value to the list
        return ans.values() #return answer.values