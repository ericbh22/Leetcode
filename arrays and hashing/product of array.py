import math

def productExceptSelf(nums):
    array = []
    prefix=  1
    suffix = sum(nums) 
    for i in range(len(nums)):
        if i != 0:
            prefix = prefix * nums[i-1]
        suffix = math.prod(nums[i+1:len(nums)])
        array.append(prefix*suffix)

    # since we are fixed, sliding window? array[0] = nums [1:-1] array[1] = nums[2:\
    # for every value that ISNT i, O(n), idk how O(1) solution is done. 
    #no division is allowed, so u cant multiply everything and divide by nums 
    # didnt work for edge cases
nums = [1,2,3,4]
productExceptSelf(nums)

"""
arraypre=[1]*len(nums)
        arraypost=[1]*len(nums)
        answer =[]
        #list of prefix
        prefix = 1
        for i in range(len(nums)):
            arraypre[i] = prefix 
            prefix *=nums[i]
        
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            arraypost[i] = suffix
            suffix *= nums[i]
            
        for i in range(len(nums)):
            answer.append(arraypre[i]*arraypost[i])
        return answer
        """