# little_sun☀
學習notes

WEEK1
=
Happy Moon Festival 🌕
-

WEEK2
=
linked-list
  -
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/linked-list.jpg)
array需要一整塊連續的記憶體空間<br>
lined-list可以由一個一個空間拼湊起來<br>
影片裡面有**新增**，nodeA = Node(數字)，nodeA.next=nodeB<br>
還有**走訪**當current.next!=none時，count就+1，不再+的話代表是最後一個，那就可以知道長度了<br>
除了上述兩個功能，還有**刪除**和**查詢**兩個功能可以操作<br>
<br>

WEEK3
=
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


WEEK4
=
set
  -
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/set.jpg)
在紙上寫出邏輯，再寫進Python<br>
我用的是老師給的方法的Approach 1: Brute Force <br>
用相同的邏輯把java換成python<br>
課堂上失敗，10/12 run code過了，submit沒過:(

Insertion Sort
  -
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/insertion_sort.jpg)
用第一個數字當作基準點，第二個往前和第一個比較，第三個往前和第二比較再和第一比較...以此類推<br>
每一次都是兩兩比較，執行效率比較慢

Quick Sort
 -
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/quick_sort.jpg)
先找一個數字設為基準點，比他大的一堆，比他小的一堆<br>
兩堆再各自有一個基準點，一樣再分大小，執行效率比較快

