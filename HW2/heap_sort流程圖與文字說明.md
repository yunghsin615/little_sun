# HeapSort


Time Complexity = Nlog^N<br>
以二元樹(Binary Tree)為基礎，分為父節點和子節點，每個父節點最多只有兩個子節點<br>
我做的是MAX Heap，每個父節點都要比他的子節點大，反之min Heap就是每個父節點都要比他的子節點小<br>
最一開始要先把Heap MAX化，這時root肯定是最大的，再把最後那個leaf跟root換，而最大的值就排進最後output值的最後一個位置<br>
這時再把這個Heap MAX化，把最後的leaf跟root換，再把這個值排進output的倒數第二個位置，就這樣排到只剩下一個數字為止<br>
<br>
<br>
### 以下的重點是如何creat a MAX Heap<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/Heapify.png)

<br>
<br>
<br>
### 以下流程圖省略每次Heapify的過程，重點在於如何sort<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HeapSort.png)

![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HeapSort2.png)
