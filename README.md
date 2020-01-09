# little_sun☀
學習notes

### WEEK1
*   放假<br>
*   Happy Moon Festival 🌕

### WEEK2
Linked List<br>
*   [Linked List](https://github.com/yunghsin615/little_sun/tree/master/Linked%20List)
*   [Linked List程式碼](https://github.com/yunghsin615/little_sun/blob/master/Linked%20List/Linked%20List.py)

### WEEK3

Stack<br>
*   [Stack](https://github.com/yunghsin615/little_sun/tree/master/Stack)
*   [Stacl程式碼](https://github.com/yunghsin615/little_sun/blob/master/Stack/155_Min%20Stack.py)


Queue<br>


### WEEK4

set
-
在紙上寫出邏輯，再寫進Python<br>
我用的是老師給的方法的Approach 1: Brute Force <br>
用相同的邏輯把java換成python<br>
課堂上失敗，10/12 run code過了，submit沒過:( 以下是錯誤的<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/wrong_set.jpg)<br>
10/15終於成功了，有點久(=･ω･=)  <br>
迴圈的for i in range()括號裡的len+1，不然不會讀取到最後一個位置的數值<br>
例如: list=[0,0,0,0]<br>
      for i in range(1,len(nums)):<br>
          print(i)<br>
      1<br>
      2<br>
      3<br>
還有for迴圈的重點要知道哪裡開始哪裡結束!<br>
一開始就沒好好搞懂邏輯才會不知道第一個for環圈的結束位置在missing=i，所以縮排才會錯<br>
最後終於submit也過了，但Time Limit Exceeded，用了兩個迴圈執行效率太差，再接再厲<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/set.jpg)


Insertion Sort
-
用第一個數字當作基準點，第二個往前和第一個比較，第三個往前和第二比較再和第一比較...以此類推<br>
每一次都是兩兩比較，執行效率比較低，但是如果剛好排序已經是從小到大的話，時間就會很快<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/insertion_sort.jpg)

### WEEK5
*   放假<br>
*   Happy Double Tenth Day <br>

### WEEK6
Quick Sort<br>
*   [HW1](https://github.com/yunghsin615/little_sun/tree/master/HW1)
*   [Quick Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW1/quick_sort.ipynb)
*   [Quick Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW1/quick_sort.jpg)<br>

Heap Sort<br>
*   [HW2](https://github.com/yunghsin615/little_sun/tree/master/HW2)
*   [Heap Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW2/heap_sort_06170236.py)
*   [Heap Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW2/heap_sort%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md)

### WEEK7
Merge Sort<br>
*   [HW2](https://github.com/yunghsin615/little_sun/tree/master/HW2)
*   [Merge Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW2/merge_sort_06170236.py)
*   [Merge Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW2/merge_sort%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md)
*   [Merge Sort & Heap Sort的比較](https://github.com/yunghsin615/little_sun/blob/master/HW2/Comparison.md)


### WEEK8
Binary Tree<br>
由Linked-List為基礎的演算法<br>
照順序排樹，第一個是root，每個父節點最多會有兩個子節點(二元)，並且在前一個父節點滿兩個小孩後，才會再往下加<br>
每個父節點都是parent，最下面的子節點是Leaf，一個點可以同時是父節點也是子節點<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/BinaryTree.jpg)

### WEEK9
Binary Search Tree<br>
*   [HW3](https://github.com/yunghsin615/little_sun/tree/master/HW3)
*   [BST程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW3/binary_search_tree_06170236.py)
*   [BST流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW3/Binary%20Search%20Tree%20%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md)
*   [BST新增、刪除、查詢、修改功能說明](https://github.com/yunghsin615/little_sun/blob/master/HW3/Binary%20Search%20Tree%E6%96%B0%E5%A2%9E%E3%80%81%E5%88%AA%E9%99%A4%E3%80%81%E6%9F%A5%E8%A9%A2%E3%80%81%E4%BF%AE%E6%94%B9%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.md)
      
### WEEK10

Red Black Tree
-
以Binary Search Tree為基礎的演算法<br>
差異是在他需要**平衡**，在insert和delete的時候，要讓整棵樹平衡<br>
首先有一些限制<br>
一:每個節點不是紅或是黑<br>
二:ROOT必須是黑<br>
三:若節點為紅，其子節點必為黑<br>
四:若節點為嘿，其子節點可為紅或黑<br>
五:每個空節點都是黑<br>
六:從ROOT到leaf的每條路徑，必包含相同數目的黑色節點<br>

![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/BRT.jpg)
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/BRT2.jpg)

### WEEK11
Hash Table<br>
*   [HW4](https://github.com/yunghsin615/little_sun/tree/master/HW4)
*   [Hash Table程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW4/hash_table_06170236.py)
*   [Hash Table流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW4/Hash%20Table%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%20Table%E8%88%87Hash%20Function%E5%8E%9F%E7%90%86.ipynb)

### WEEK12
Breadth-First Search<br>
*   [HW5](https://github.com/yunghsin615/little_sun/tree/master/HW5)
*   [BFS程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS_06170236.py)
*   [BFS流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)
<br>

### WEEK13
Depth-First Search<br>
*   [HW5](https://github.com/yunghsin615/little_sun/tree/master/HW5)
*   [DFS程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS_06170236.py)
*   [DFS流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)

### WEEK14
Minimum Spanning Tree<br>
*   [HW6](https://github.com/yunghsin615/little_sun/tree/master/HW6)
*   [MST程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW6/Dijkstra_06170236.py)
*   [MST流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW6/Dijkstra%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)

### WEEK15
Shortest Path<br>
*   [HW6](https://github.com/yunghsin615/little_sun/tree/master/HW6)
*   [Shortest Path程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW6/Dijkstra_06170236.py)
*   [Shortest Path流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW6/Dijkstra%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)

### WEEK 16
*   Overview

### WEEK17
*   Final

### WEEK18
*   放假<br>
*   回家投票~~~<br>
