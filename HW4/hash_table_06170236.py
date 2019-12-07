from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        
        code = MD5.new()
        code.update(key.encode("utf-8"))
        number = int(code.hexdigest(),16)
        index = number % self.capacity
        
        if self.data[index] == None:
            self.data[index] = ListNode(number)
            
        else:
            new_node = ListNode(number)
            new_node.next = self.data[index]
            self.data[index] = new_node
            
    def remove(self, key):
        
        while self.contains(key) != False:
            code = MD5.new()
            code.update(key.encode("utf-8"))
            number = int(code.hexdigest(),16)
            index = number % self.capacity
            blank = self.data[index]
            
            if blank.val == number:
                self.data[index] = blank.next
                self.remove(key)
                return
            
            pointer = None
            while blank: 
                if blank.val == number and blank.next:
                    pointer.next = blank.next
                    break
                
                elif blank.val == number and blank.next is None:
                    pointer.next = None
                    break
                    
                elif blank.val != number:
                    pointer = blank
                    blank = blank.next
                    
            self.remove(key)
            
        if self.contains(key) == False:
            return
        
    def contains(self, key):
        
        code = MD5.new()
        code.update(key.encode("utf-8"))
        number = int(code.hexdigest(),16)
        index = number % self.capacity
        blank = self.data[index]
        
        if blank == None:
            return False
        
        else:
            while blank:
                if blank.val == number:
                    return True
                
                elif blank.val != number:
                    blank = blank.next
            
                    if blank == None:
                        return False
