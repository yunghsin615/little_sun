class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inputStack = []
        self.resStack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.inputStack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.inputStack:
            a = self.inputStack[0]
            self.inputStack.pop(0)
            return a

  
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.inputStack:
            return self.inputStack[0]

   
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.inputStack) == 0:
            return True
        return False
