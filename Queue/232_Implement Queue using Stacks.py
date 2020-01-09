class MyQueue(object):

    def __init__(self):
        
        self.inputStack = []

    def push(self, x):
        
        self.inputStack.append(x)

    def pop(self):
        
        if self.inputStack:
            a = self.inputStack[0]
            self.inputStack.pop(0)
            return a

    def peek(self):

        if self.inputStack:
            return self.inputStack[0]

    def empty(self):

        if len(self.inputStack) == 0:
            return True
        return False
