class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #so we are given a histogram and asked to find the largest rectangle IN the histogram
        # rectangle can span more than one block , so to calcualte recatangle hiehgt we are always going to be doing the index * lower of the 2
        # the lower of the 2 can be kept up with a monotonic stack, so can the current highest? 
        # we cant sort here cuz that would mess up the order, we need this order
        # if u ever get a rectangle thats > u need to consider popping
        # so if i got 2,1,5 as soon as i see the 5 i needa consider getting rid of 2,1
        # consider cases 5,6,7 and 7,6,5 , u can have 15 or u can have 12, how should we deal with that
        #monotonic stack of areas or monotnic stakc of heights we can have is the big issue rn i think 
        # all combinations of 1,2,3 kinda makes sense 
        #  brute force is triyng 2,1 2,1,5 2,1,6 etc
        #then  u get to 1 which is always just +1
        # then u get to 5 which is 5,5 5,2 5,3, with this one as soon as u see the number has dropped less tahn 5, there is no need tot est that number, we need to test for as long as the next number is bigger than 5, so whe  the top of the stakc is > 5 we keep going, doesnt sound very stacky tho cuz we need reference to the first element? 
        # would we test something like 4,3 ? we probabaly should ut that breaks our idea of not testing anything smaller 
        # there is also a reaosn to not stop testing, cuz of 7,6,5 and 5,6,7 even tho its smaller the 5 is biger area 
        # lets say we have 1,6,4 and 5,6,4 obviously triple 5 is best, so after testing 6,4 we should not need to test anything else, if its less than our current max no need to test? 
        # where doesthe stack come in ? 
        # you gotta test consecutives so if its not  smaller dont cut it ? this is a clear o ( n squared ) solution
        # test 7, test 7,6 test 7,6,5 until the result is smaller, then stop testing and pop 7, test the next number
        #test 2 , test 2,1 test 2,1,5 3 is still better than 2, but its time to cut.. 
        stack = [] 
        for i in range(len())