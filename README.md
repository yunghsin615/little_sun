# little_sun☀
學習notes

### WEEK1
*   放假<br>
*   Happy Moon Festival 🌕<br>

### WEEK2

linked-list
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/linked-list.jpg)
array需要一整塊連續的記憶體空間，刪除需要整塊做調整<br>
lined-list可以由一個一個空間拼湊起來，這樣刪除的話，就不用整塊調整<br>
影片裡面有**新增**，假如我要新增2，nodeA = Node(2)，nodeA.next=nodeB，也就是nodeA -> nodeB<br>
還有**走訪**當current.next!=none時，count就+1，不再+的話代表是最後一個，那就可以知道長度了<br>
除了上述兩個功能，還有**刪除**和**查詢**兩個功能可以操作<br>
<br>

### WEEK3

Stack &  Queue
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/stack&queue.jpg)
Stack
-
像堆盤子，最後一個放在top，使用在undo回到上一部的功能，後進先出<br>
Push(data) - 把資料放進最上方<br>
Pop - 刪除在最上方的資料<br>
Top - 回傳最上方的資料<br>
IsEmpty - 確認Stack裡面是否有資料<br>
getSize - 回傳Stack裡的資料個數

Queue
-
像排隊，最後一個放入的在隊伍最後面，先進先出<br>
Push(data) - 把資料放在最後方<br>
Pop - 刪除在最前方的資料<br>
getFront - 回傳最前方的資料<br>
getBack - 回傳最後方的資料<br>
IsEmpty - 確認Queue裡面是否有資料<br>
getSize - 回傳Queue裡的資料個數


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
*   [HW1](https://github.com/yunghsin615/little_sun/tree/master/HW1)
*   [Quick Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW1/quick_sort.ipynb)
*   [Quick Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW1/quick_sort.jpg)<br>
<Br>

Heap Sort<br>
*   [HW2](https://github.com/yunghsin615/little_sun/tree/master/HW2)
*   [Heap Sort程式碼](https://github.com/yunghsin615/little_sun/blob/master/HW2/heap_sort_06170236.py)
*   [Heap Sort流程圖](https://github.com/yunghsin615/little_sun/blob/master/HW2/heap_sort%E6%B5%81%E7%A8%8B%E5%9C%96%E8%88%87%E6%96%87%E5%AD%97%E8%AA%AA%E6%98%8E.md)
*   


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
Hash Table
-
Array+Linked-List為基礎的演算法<br>
首先，將文字或數字用一個經過Hash Function加密轉換成一串數字或一串有英文和數字的密碼<br>
那個函式是可以自己設計的，但這個作業我們使用現成的MD5來加密<br>
也因為MD5的關係，先將測值轉換成十六進位，再用int變成十進位，密碼就會變成純數字了！而且同一段文字每次出來的結果會相同<br>
再來，我的作法是將這個密碼除以要幾個抽屜，再取餘數，代表它該放進幾號抽屜<br>
如果函式處理得好，每個抽屜放一個東西的狀態是最好的<br>
如果有兩個密碼要放進同一個抽屜的事情發生，這叫做"碰撞"<br>
最後，最重要的就是要用Linked-List的方法將這些node串聯起來<br>
<br>
Hash Function(雜湊函式)<br>
這是加密過程要經歷的過程，它將複雜的文字透過函式轉換成密碼<br>
用甚麼國家的語言都可以，但要讓他知道是用甚麼編碼，像中文就是用utf-8<br>
老師說這是國際通用的，各個國家互相決定的編碼<br>
如果設計符合狀態的函式，最好的結果式每個抽屜只有一個東西<br>
這樣remove、contains花費的時間就會比較少，因為找到抽屜，然後抽屜裡有東西，就代表找到值了<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HashTable.jpg)

### WEEK12
Breadth-First Search
-
queue為基礎的演算法<br>
首先會有Adjacency List，就是把每個點的臨邊點都標示出來<br>
我們的initial狀態是self.graph = defaultdict(list)，意思是我們後來的self.graph[u]是list的狀態<br>
後面就可以直接用append(v)的方式加入，u是各個點，v是u的每個臨邊點<br>
BFS是用之前老師上課教得queue的方式，先進先出的一個概念<br>
所以每個臨邊點放在status1的時候，順序還是從第0位(status[0])開始走訪<br>
每走訪一個點(u)，就再把沒有被走訪過的臨邊點(v)加進status1，有個原則是status1和status2的值不能重複<br>
就這樣到迴圈結束<br>
![](https://i.imgur.com/vFw57lw.jpg) 1->2->3->4->5->6->8->7<br>

### WEEK13
Depth-First Search
-
stack為基礎的演算法<br>
首先會有Adjacency List，把每個點的臨邊點都標示出來<br>
DFS是用以前老師教得stack的方式，後進先出的一個概念<br>
臨邊點放進status1的順序還是照Adjacency List，但是是從最後一位(status1[-1])開始<br>
每走訪一個點(u)，就再把沒有被走訪過的臨邊點(v)加進status1，原則是status1和status2的值不能重複<br><br>
把每個點的臨邊點push進status1時，就要pop一個出來(status1[-1])，直到迴圈結束<br>
![](https://i.imgur.com/vFw57lw.jpg) 1->2->4->5->8->3->6->7<br>

### WEEK14
Minimum Spanning Tree
-
最小生成樹是把每個點都連在一起，但不能形成loop，也就是不能形成三角形這種圍成一圈的圖形<br>
設兩個list，初始狀態一個全部都-1，一個是空的<br>
因為每個edge照理來說都要測過，所以迴圈的限制是g.graph的長度<br>
再來分成兩個大項<br>
一:兩個點的root一樣<br>
又分為1.兩個點的root都是-1、2.兩個點的root都不是1<br>
二:兩個點的root不一樣<br>
又分為1.其中一個點的root是-1、2.兩個點的root不一樣但都不是-1<br>
每次迴圈都會把要連結的edge的weight加進test<br>
每次連結起來的點都要換成同個root，意思是他們現在連成一條線<br>
所以當有兩條不同root的線要連在一起時，其中一條的所有root要全部換成跟另一條一樣的root，代表成為同一條線了<br>
diction的key是放起點到終點，value是放test的最後一項，也就是新加入的值<br>
最後當有n個點的時候，就應該要有n-1個edge，這時迴圈結束<br>
實際應用像是連結城市的通訊網，可以計算最低成本<br>
{'1-4': 1, '4-6': 2, '0-5': 3, '0-1': 5, '2-3': 5, '3-4': 7} <br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/MST.jpg)

### WEEK15
Shortest Path
-
最短路徑的運算就是給一個起點(s)，計算他到每個點的最短路徑<br>
設兩個list，初始狀態一個全部點都是無限(dist)，另一個都是False(test)，這是為了檢測各點是否已經被走過了<br>
迴圈設while test != [True] * self.V，也就是代表還沒有把所有點走完<br>
再來助教給的測資的0是自己到自己的路徑，或是點不在隔壁的路徑<br>
所以當條件一:g.graph不等於0，和條件二:dist[現在點的index] + g.graph小於原來的dist[0-self.V的index]<br>
兩個條件都達成的時候，dist[0-self.V的index]會等於dist[現在點的index] + g.graph，因為路徑更短<br>
接下來就是找test=False(還沒被走過)的情況下，dist裡面最小的那個點<br>
找出最小的點和那個點的index，再把test[index]變成True<br>
最後dist就是從起點開始到各點的最短路徑，把它變成dictionary的形式就完成了<br>
{'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/SP.jpg)

### WEEK 16
Overview
-

### WEEK17
Final
-

### WEEK18
放假<br>
回家投票~~~<br>
