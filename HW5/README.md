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

Depth-First Search
-
stack為基礎的演算法<br>
首先會有Adjacency List，把每個點的臨邊點都標示出來<br>
DFS是用以前老師教得stack的方式，後進先出的一個概念<br>
臨邊點放進status1的順序還是照Adjacency List，但是是從最後一位(status1[-1])開始<br>
每走訪一個點(u)，就再把沒有被走訪過的臨邊點(v)加進status1，原則是status1和status2的值不能重複<br><br>
把每個點的臨邊點push進status1時，就要pop一個出來(status1[-1])，直到迴圈結束<br>
![](https://i.imgur.com/vFw57lw.jpg) 1->2->4->5->8->3->6->7<br>
