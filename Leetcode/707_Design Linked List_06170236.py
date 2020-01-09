class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.size == 0:
            return -1
        
        elif index < 0 or index >= self.size:
            return -1
        

        pointer = self.head
        for i in range(index):
            pointer = pointer.next
        return pointer.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = Node(val)
        
        else:
            node = Node(val)
            node.next = self.head
            self.head = node
            
        self.size+=1
   
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = Node(val)
        
        else:
            pointer = self.head
            while pointer.next!=None:
                pointer = pointer.next
            else:
                pointer.next = Node(val)
                
        self.size+=1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.head = Node(val)
            
        else:
            if index == 0:
                self.addAtHead(val)
                
            elif index == self.size:
                self.addAtTail(val)
                
            elif index < 0 or index >self.size:
                return
            
            else:
                pointer = self.head
                for i in range(index-1):
                    pointer = pointer.next
                node = Node(val)
                node.next = pointer.next
                pointer.next = node
                
        self.size+=1
       

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.size == 0:
            return
        
        if index < 0 or index >= self.size:
            return
        
        else:
            pointer = self.head
            if index == 0:
                self.head = pointer.next
                
            else:
                for i in range(index-1):
                    pointer = pointer.next
                pointer.next = pointer.next.next

        self.size-=1
        
