
class Solution(object):
    def topKFrequent(self, nums, k):
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # array of integers
        # return the k most frequest elements, not how many times they occured
        # u can maybe use a hashmap, then u can get the values of the hashmap ? or potentially slide windows of different sizes? or simply just an array holding the max?

        # mydict = defaultdict(int)
        # largest = []
        # for i in (nums):
        #     mydict[i] = 1 + mydict.get(i,0)
        
    
        # sortedlist = sorted(mydict, key=mydict.get, reverse=True)
        # for i in range(k):
        #     largest.append(sortedlist[i])
        # return largest  

        # can get faster, my solution adds them to a dictionary, then sorts the dictionary 
        #this second apporach is faster at the cost of memory as it uses a frequency tracker, frequency of the len at the front and it checks 
        #bucket sort modified 
        mydict = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            mydict[n]= 1+ mydict.get(n,0)
        for n,c in mydict.items():
            freq[c].append(n)
        res=[]
        for i in range(len(freq)-1,0,-1): # we go backwards here for that reason
            for n in freq[i]: #struff will be empty so it wont append 
                res.append(n)
                if len(res) ==k: 
                    return res