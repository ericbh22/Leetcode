class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #car flets speed is the speed of the lowest
        #not every car will be in the car fleet because if ur faster, u will never slow downt o be in the car fleet, if ur slower u will never make it into the fleet
        # so how do we manage this? 
        #note that the positions are not in order? i feel like if they were this would be much easier
        # so a car starting at position can go forwards w a certain speed 
        #the furthest out is 10 at 2, so then 8 at 4 defo can, and 3 at 3 defo can. we needa find the person furthest out first and then check everyone else
        # so the question is do we check back to front, or front to back
        # or can we check in order !? like daily temperatures, monotonic stack? 
        # there is also a target so  we cant just go crazy forever 
        # multiple fleets can be formed before we arrive at our location
        # we look by speed, and then we consider their positions. so we see two speed 1's then we consider if they can ever mee thte speed 2's 
        # also need a general formula to look if two postion will collide before a given point 
        # dont deep it, what if we just pushed onto our stack
        # 10,8,0 
        # what speed would u need for 0 to be possible, what speed would u need for 8 to be possible
        # if 0 is impossible, pop 10,8 then push 0, then start a new
        # everytime something is impossible, clear the stack 
        stack = [] 
        for i in range(len(position)):
            if i == 0:
                stack.append(position[i])
            elif: