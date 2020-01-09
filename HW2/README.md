Heap Sort
-
Time Complexity = Nlog^N<br>
以二元樹(Binary Tree)為基礎，分為父節點和子節點，每個父節點最多只有兩個子節點<br>
我做的是MAX Heap，每個父節點都要比他的子節點大，反之min Heap就是每個父節點都要比他的子節點小<br>
最一開始要先把Heap MAX化，這時root肯定是最大的，再把最後那個leaf跟root換<br>
而最大的值就排進最後output值的最後一個位置這時再把這個Heap MAX化，把最後的leaf跟root換<br>
再把這個值排進output的倒數第二個位置，就這樣排到只剩下一個數字為止<br>

如何creat a MAX Heap<br>
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/Heapify.png)

如何Heap sort<br>
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HeapSort.png)

![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HeapSort2.png)


Merge Sort
-
Time Complexity = Nlog^N
每次都把一個數列分為兩堆，直到剩下1個為止，不像QuickSort會有選pivot的運氣問題，而是成穩定的時間狀態<br>
一個數字和一個數字比較後合併成兩個數字的數列，兩個數字和兩個數字比較後合併成四個數字的數列...以此類推<br>
一層一層合併到變成原本的長度就結束了，然後這時數字要是按照排列的<br>
我會把它拆解成兩個部分來看，第一部分是sort，分堆後比大小的過程<br>
第二部分是merge，比完大小並把他們匯集成同個陣列的過程<br>
其實雖然說是拆成兩個部分來看，但它們的意義沒有完全被分開<br>
<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/MergeSort.png)
