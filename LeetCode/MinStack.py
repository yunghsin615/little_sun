class Node:
    def __init__(self, val):
        self.val = val
        self.temp_min = val
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        
    def push(self, x):
        if len(self.arr) == 0:
            self.arr.append(x)
            self.temp_min = x
        else:
            self.arr.append(x)
            if self.temp_min > self.arr[-1]:
                self.temp_min = self.arr[-1]


    def pop(self):
        """
        :rtype: None
        """
        self.arr.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.arr[-1]

    def getMin(self):
        """
        :rtype: int
        """
        sort = sorted(self.arr)
        return sort[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
