class Solution:
    def trap(self, height) -> int:
        #to calculate how much can be trapped, in a small case such as [2,1,0,1,3] what should we do? we know the answer in this scenario is 4 
        # we know 1,0,1 is tgoing to be 1, and 2,0,2 would be 2, 
        # but we know trapping something doesnt always rqure a 0, for example 2,1,2 would trap 1, we know that we just need a dip between 2 things that are of same hiehgt or taller
        # so we need 2 pointers to check for dips 
        # we do not need both pointers to point to the same value
        # for example if we had        
        # two points starting at the same place, until u get to one bigger then u can decide how to work it, w a sum running in betwee
        # maybe try an o n squared approach 
        totalwater = 0
        curroccupied = 0 
        visited = []
        for i in range(len(height)):
            if i in visited:
                continue
            for j in range(i+1,len(height)):
                if height[j] >= height[i]:
                    area = height[i] * (j-i-1)-curroccupied
                    totalwater += area
                    print(f"{i} and {j} and {totalwater} and {area} and {curroccupied}")
                    curroccupied =0
                    # deal w the issue of that big 3 that never finds another
                    break 
                else: 
                    curroccupied += height[j] 
                    visited.append(j)
                if j == len(height) - 1:
                    curroccupied =0
                    visited.clear()
                    print(visited)
                    #  do nothing if we rteach the end 
                # if we reached the end, 
                # new issue is that we are double counting element
                #array to check if we visited that index 
        return totalwater 
solution = Solution()
tester = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])

