#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        
        number = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        index = number % self.capacity
        
        if self.data[index] == None:
            self.data[index] = ListNode(number)
            
        else:
            new_node = ListNode(number)
            new_node.next = self.data[index]
            self.data[index] = new_node
            
    def remove(self, key):

        while self.contains(key) != False:
            number = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
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

        number = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
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


# 參考資料：<br>
# https://www.cs.wcupa.edu/rkline/ds/hash-sets.html<br>
# https://www.runoob.com/python/func-number-abs.html #絕對值<br>
# https://blog.csdn.net/qq_40587575/article/details/82431806 #return用法<br>
# https://github.com/yunghsin615/little_sun/blob/master/LeetCode/linked_list.py #我自己的linked-list<br>
