linked-list
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/linked-list.jpg)
array需要一整塊連續的記憶體空間，刪除需要整塊做調整<br>
lined-list可以由一個一個空間拼湊起來，這樣刪除的話，就不用整塊調整<br>
影片裡面有**新增**，假如我要新增2，nodeA = Node(2)，nodeA.next=nodeB，也就是nodeA -> nodeB<br>
還有**走訪**當current.next!=none時，count就+1，不再+的話代表是最後一個，那就可以知道長度了<br>
除了上述兩個功能，還有**刪除**和**查詢**兩個功能可以操作<br>
