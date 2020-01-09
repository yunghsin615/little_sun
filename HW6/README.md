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
