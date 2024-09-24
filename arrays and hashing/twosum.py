class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # currp = 0
        # while currp != len(nums):
        #     for i in range(len(nums)-1,currp-1,-1):
        #         if nums[currp]+nums[i] == target:
        #             return currp , i
        #     currp +=1

        # do target - the number and check if its in the list, can use set asw? 
        # hashset = set()
        # for i in nums:
        #     hashset.add(i)
        # for i in hashset:
        #     if target-i in hashset:
        #         return ()
        # return False 
        # puts index and value in 
        hashmap = {} # doesnt work for duplicate values 
        for i,j in enumerate(nums):
            if (target - j) in hashmap: #if the target - j in hashmap 
                return(hashmap[target-j],i)
            hashmap[j]=i
