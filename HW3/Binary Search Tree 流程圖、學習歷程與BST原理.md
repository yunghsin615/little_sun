Binary Search Tree(二元搜尋樹)
=
首先，加入的第一個值會是這個樹的root<br>
再接下來新增的值就會依照**比root小或等於root就往left擺**和**比root大就往right擺**的原則建立一個Tree<br>
相較於上次作業的heap的Binary Tree，差別是Binary Tree一定是有兩個child，才會往下個位置擺node<br>
Binary Search Tree則是可以只有一個child，然後那個child可能還有一個或兩個child<br>
那為什麼要建立Binary Search Tree?<br>
如果我們有非常大量的資料，就可以依照**比root小或等於root就往left擺**和**比root大就往right擺**的原則來做不管是搜尋、刪除或修改的這些動作，這樣就不需要把全部的資料掃過一遍，而是有脈絡的去找到那個node，耗費的時間會比較短<br>
<br>
我的學習歷程是先從第一週教的linked-list開始<br>
前幾週都覺得沒辦法理解，完成後就覺得也沒那麼難嘛，我的方法是先有大概的想法再手寫，最後才打程式，幾乎沒有錯誤<br>
好的，以下是我linked-list的程式碼<br>
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
        
流程圖<br>
=

insert新增<br>
-
我insert一個2，流程圖的說明直接手寫在上面<br>
大概就是小於等於2的時候，往左邊找位子，大於2的時候，往右邊找位子<br>
找到位子的時候他就會建一個Treenode(2)在那邊<br>
<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/insert.jpg)
<br>
<br>
<br>
search搜尋<br>
-
我search一個2.5<br>
也是小於等於2.5的時候，往左邊找，大於2.5的時候，往右邊找<br>
因為建樹的時候都有按照這個原則，所以tree裡面有2.5的話，就一定找的到<br>
然後我再搜尋一個3.5<br>
小於等於3.5的時候，往左邊找，大於3.5的時候，往右邊找<br>
一樣，建樹的時候都有按照這個原則，所以tree裡面的指向==None的時候，代表沒有這個數字，不可能會在別的位置上<br>
<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/search.jpg)
<br>
<br>
<br>
delete刪除<br>
-
我delete寫了四種可能，但實際上超級多種可能，看我的def寫了160行就知道了<br>
我寫的四種可能:1.刪除值沒有child 2.刪除值只有右邊的child 3.刪除值只有左邊的child 4.刪除值有兩邊的child<br>
寫delete真的是重重關卡，一直以為寫完了，然後測不同的值，就又發現漏洞<br>
卡最久的地方是刪除root而且它只有一個child的時候，這時候的可能性會有超級多!!!<br>
拜託拜託，希望所有可能我都有想到了ಥ_ಥ<br>
<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/delete.jpg)
<br>
<br>
參考資料:<br>
https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm<br>
http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html<br>
http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html<br>
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/<br>
https://medium.com/@stephenagrice/how-to-implement-a-binary-search-tree-in-python-e1cdba29c533<br>
