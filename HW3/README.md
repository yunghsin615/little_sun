Binary Search Tree
-
由Linked-List為基準的演算法<br>
首先，加入的第一個值會是這個樹的root<br>
再接下來新增的值就會依照比root小或等於root就往left擺和比root大就往right擺的原則建立一個Tree<br>
相較於上次作業的heap的Binary Tree，差別是Binary Tree一定是有兩個child，才會往下個位置擺node<br>
Binary Search Tree則是可以只有一個child，然後那個child可能還有一個或兩個child<br>
那為什麼要建立Binary Search Tree?<br>
如果我們有非常大量的資料，就可以依照比root小或等於root就往left擺和比root大就往right擺的原則來做不管是搜尋、刪除或修改的這些動作<br>
這樣就不需要把全部的資料掃過一遍，而是有脈絡的去找到那個node，耗費的時間會比較短<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/BST.png)
