# little_sun☀
*   姓名:陳永欣
*   學校:東吳大學
*   系級:巨資三B
*   這是是放資料結構與演算法課程的learning notes

# Data Structure and Algorithm 
在剛開學的時候，老師以為大家都知道GitHub，他說這是工程式的FaceBook，但大家幾乎都不知道，不過後來慢慢在很多進階課程都持續有聽到。整個學期幾乎都在寫一份又一份的作業，每次都覺得自己終於寫完了很厲害，然後就發現助教測資又沒過，這堂課讓大家學了不少也老了不少，終於放寒假可以休息一下，但還是要持續精進自己的技能吧!<br>

### WEEK1
*   放假<br>
*   Happy Moon Festival 🌕

### WEEK2
Linked List<br>
基本演算法，不需要連續的記憶體空間，一開始沒辦法寫出程式碼，到後面要應用前補回來，發現其實是很簡單的道理<br>
*   [Linked List](https://github.com/yunghsin615/little_sun/tree/master/Linked%20List)
*   [Linked List程式碼](https://github.com/yunghsin615/little_sun/blob/master/Linked%20List/Linked%20List.py)

### WEEK3
Stack<br>
基本演算法，像盤子一層一層疊上去，Last in first out<br>
*   [Stack](https://github.com/yunghsin615/little_sun/tree/master/Stack)
*   [Stack程式碼](https://github.com/yunghsin615/little_sun/blob/master/Stack/155_Min%20Stack.py)

Queue<br>
基本演算法，像排隊一個一個往後排，first in first out<br>
*   [Queue](https://github.com/yunghsin615/little_sun/tree/master/Queue)
*   [Queue程式碼](https://github.com/yunghsin615/little_sun/blob/master/Queue/232_Implement%20Queue%20using%20Stacks.py)

### WEEK4
Set<br>
找重複值和缺失值，老師上課教了一種方式，也提供我們另外5種，我選了一種打在Leetcode，但是他說Time Limit Exceeded<br>
雖然觀念是對的，但是時間太久了，詳細細節在下面的連結<br>
*   [Set](https://github.com/yunghsin615/little_sun/tree/master/Set)
*   [Set程式碼](https://github.com/yunghsin615/little_sun/blob/master/Set/645_Set%20Mismatch.py)

Insertion Sort<br>
*   [Insertion Sort](https://github.com/yunghsin615/little_sun/tree/master/Insertion%20Sort)

### WEEK5
*   放假<br>
*   Happy Double Tenth Day <br>

### WEEK6
Quick Sort<br>
往前一個位子比較，比自己大就再往前，比自己小就可以插入，平均時間複雜度高，且不穩定<br>
*   [HW1](https://github.com/yunghsin615/little_sun/tree/master/HW1)
*   [Quick Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW1/quick_sort.ipynb)
*   [Quick Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW1/quick_sort.jpg)<br>

Heap Sort<br>
想成一個tree的狀態，建立MAX Heap再把最大的root換到最後一個位子，等於是放在list的最後一位，不另外占空間<br>
*   [HW2](https://github.com/yunghsin615/little_sun/tree/master/HW2)
*   [Heap Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW2/heap_sort_06170236.py)
*   [Heap Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW2/heap_sort%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md)

### WEEK7
Merge Sort<br>
先將全部的值分成一個一個看，兩組兩組比較，小的擺前，大的擺後，穩定的狀態<br>
*   [HW2](https://github.com/yunghsin615/little_sun/tree/master/HW2)
*   [Merge Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW2/merge_sort_06170236.py)
*   [Merge Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW2/merge_sort%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md)
*   [Merge Sort & Heap Sort的比較](https://github.com/yunghsin615/little_sun/blob/master/HW2/Comparison.md)


### WEEK8
Binary Tree<br>
從root開始，每個node可以有兩個child，位子比較前的接兩個child後，才會換下個接<br>
root是parent，沒有child的是leaf，其他的node都是同時是parent也是child<br>
*   [Binary Tree](https://github.com/yunghsin615/little_sun/tree/master/Binary%20Tree)

### WEEK9
Binary Search Tree<br>
從root開始，比他大的往右邊放，比他小的往左邊，接的每個node都要比大小<br>
跟Binary Tree不一樣的是，可能parent只有一個child<br>
*   [HW3](https://github.com/yunghsin615/little_sun/tree/master/HW3)
*   [BST程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW3/binary_search_tree_06170236.py)
*   [BST流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW3/Binary%20Search%20Tree%20%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BST%E5%8E%9F%E7%90%86.md)
*   [BST新增、刪除、查詢、修改功能說明](https://github.com/yunghsin615/little_sun/blob/master/HW3/Binary%20Search%20Tree%E6%96%B0%E5%A2%9E%E3%80%81%E5%88%AA%E9%99%A4%E3%80%81%E6%9F%A5%E8%A9%A2%E3%80%81%E4%BF%AE%E6%94%B9%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.md)
      
### WEEK10
Red Black Tree<br>
非常困難，比Binary Search Tree多了平衡，新增要平衡，刪除也要平衡<br>
*   [BRT](https://github.com/yunghsin615/little_sun/tree/master/Red%20Black%20Tree)

### WEEK11
Hash Table<br>
每個值都要放進一個抽屜裡，最好是每個抽屜只有一個值，時間複雜度就會是1<br>
每個抽屜是用array的方式連結，但如果有同時兩個值要放進同個抽屜，就會用linked list的方式連結<br>
*   [HW4](https://github.com/yunghsin615/little_sun/tree/master/HW4)
*   [Hash Table程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW4/hash_table_06170236.py)
*   [Hash Table流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW4/Hash%20Table%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%20Table%E8%88%87Hash%20Function%E5%8E%9F%E7%90%86.ipynb)

### WEEK12
Breadth-First Search<br>
Queue的應用，不同的起點會有不同的路徑，但一樣first in first out<br>
*   [HW5](https://github.com/yunghsin615/little_sun/tree/master/HW5)
*   [BFS程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS_06170236.py)
*   [BFS流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)
<br>

### WEEK13
Depth-First Search<br>
Stack的應用，不同的起點會有不同的路徑，但一樣last in first out<br>
*   [HW5](https://github.com/yunghsin615/little_sun/tree/master/HW5)
*   [DFS程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS_06170236.py)
*   [DFS流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW5/BFS%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)

### WEEK14
Minimum Spanning Tree<br>
最小生成樹，把所有點連起來，並且是最小的成本，例如送貨，每個點都要走到，考慮時間或路徑長的成本<br>
*   [HW6](https://github.com/yunghsin615/little_sun/tree/master/HW6)
*   [MST程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW6/Dijkstra_06170236.py)
*   [MST流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW6/Dijkstra%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E3%80%81%E6%B5%81%E7%A8%8B%E5%9C%96.ipynb)

### WEEK15
Shortest Path<br>
最短路徑，跟上面不一樣的是會有一個起點，他到每個點的最短路徑為何?算完後會知道走怎樣的路徑到達目的地是花最小成本的<br>
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
