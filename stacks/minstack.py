class MinStack:

    def __init__(self):
        self.list = []
        self.min = {}
        self.length = 0 
# self. prevmin is not the way , its just not gunna work out for dupes
# potenitally need more, something like a list that stores the values as we go
# like the min for each state needs to be updated?
# a dictionary with states stored

    def push(self, val: int) -> None:
        self.list.append(val)
        if self.length ==  0 : # maybe this is the issue, self.min is not none
            self.min[0] = val  
        else:
            if val <= self.min[self.length-1]:
                self.min[self.length] = val
            else:
                self.min[self.length] = self.min[self.length-1]
        self.length += 1  


    def pop(self) -> None:
        self.length-=1
        self.list.pop()
        
            
            

    def top(self) -> int:
        return self.list[-1]
        

    def getMin(self) -> int:
        return self.min[self.length-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()