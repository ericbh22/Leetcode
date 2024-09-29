class Solution:
    def maxArea(self, height: List[int]) -> int:
        #[1,8,6,2,5,4,8,3,7]
        #the first question we hve is why is it not 8 and 8
        # in that case, the height is index 1 and index 6, giving us a distance of 5 so 40 area
        #where as we have indedx 1 vs index 8 giving us length 7 with height of 7. you always take the min, and then you get the length 
        # feels very similar to two sum, but the issue is you dont have a target, so you odnt know how to move 
        #we can definitely do this like a 3 sum?, hold one constant but thtas not really 2 pointer
        # can we repeat it twice, after one time we will definitely find one of the highest? 
        # maybe works, idk
        ia = 0
        ib = len(height) -1
        # maxvol = -1
        # while ia<ib:
        #     currentvol = (ib-ia)*(min(height[ia],height[ib]))
        #     if currentvol > maxvol:
        #         maxvol = currentvol
        #         currleft = ia 
        #     ia +=1
        # ia = currleft
        # while ib>ia:
        #     currentvol = (ib-currleft) * (min(height[ia],height[ib])) #one extra operation done here doubling up
        #     if currentvol > maxvol:
        #         maxvol = currentvol
        #         currright =ib
        #     ib -=1
        # return maxvol
        maxvol = -1
        while ia<ib:
            currentvol = (ib-ia)*(min(height[ia],height[ib]))
            if currentvol > maxvol:
                maxvol = currentvol 
            if height[ia] > height[ib]:
                ib-=1
            else:
                ia+=1 
        return maxvol