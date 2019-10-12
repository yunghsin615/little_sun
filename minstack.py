class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.temp_min = val
        self.next = nextNode
        
    
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.\
        """

        self.topNode = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.topNode == None:
            self.topNode = Node(x,None)
        else:
            temp = self.topNode.temp_min
            self.topNode = Node(x,self.topNode)
            if temp < self.topNode.val:
                self.topNode.temp_min = temp
        
    def pop(self):
        """
        :rtype: None
        """
        self.topNode = self.topNode.next

    def top(self):
        """
        :rtype: int
        """
        return self.topNode.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.topNode.temp_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
