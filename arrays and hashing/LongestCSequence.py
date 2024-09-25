class Solution:
    def longestConsecutive(self, nums):
       #longest consecutive is just sort, and then look at it, the thing is our look at it runs in O(n)?
       #cant use sorted because its n log n, we need one traversal
        noDups = set()
        myDict = {}
        maxlength = 1
        sortedlist = []
        for j in nums:
                noDups.add(j)
        for j in noDups:
           myDict[j] = 1+ myDict.get(j,0)
        while len(noDups) > 0:
            for k in noDups:
            #probabaly still too slow cuz if we get a three, we dont know if we r gunna get a 2 later? just search for one less one higher
            #what if theres like a 3,4,6,7,8,9,5 scenario ? without using .sort this seems hard 
            #even worse, 3,4,10,11,12,13,14,15,5 we would reject all the 10,11,12,13,14 cuz they dont match our 3 setup? we need to find what 10 is? so we can add 3,4,5 into our sorted list, if its not in our sorted list start a new sortedlist?, try all combos for 3, when we check 4 we know its cooked
            #we can make a bunch of sortedlists actually, with a boundary, appane dhtem all to the one list? cuz we can remove physically from nums 
                sortedlist.append(k)
                if k+1 in noDups:
                    noDups.remove(k+1)
                    sortedlist.append(k+1)
                if k-1 in noDups:
                    noDups.remove(k-1)
                    sortedlist.append(k+1)z

                #after u do this, save hte lenght of this sorted list, and clear it and go again 

                
    

nums = [100,4,200,1,3,2]
        
Tester = Solution()
result = Tester.longestConsecutive(nums)