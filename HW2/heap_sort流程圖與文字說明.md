# HeapSort

Time Complexity = Nlog^N<br>
以二元樹(Binary Tree)為基礎，分為父節點和子節點，每個父節點最多只有兩個子節點<br>
我做的是MAX Heap，每個父節點都要比他的子節點大，反之min Heap就是每個父節點都要比他的子節點小<br>
最一開始要先把Heap MAX化，這時root肯定是最大的，再把最後那個leaf跟root換<br>
而最大的值就排進最後output值的最後一個位置這時再把這個Heap MAX化，把最後的leaf跟root換<br>
再把這個值排進output的倒數第二個位置，就這樣排到只剩下一個數字為止<br>
<br>
<br>
### swap
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/def_swap.jpg)
因為會很常用到這個功能，所以先定義，這樣版面才不會太亂(⁎⁍̴̛ᴗ⁍̴̛⁎)<br>
<br>
<br>
### heapify
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/def_heapify.jpg)
MAX = i 目前MAX這個位置放在i這邊<br>
L,R = i*2+1,i*2+2 L是左子節點，R是右子節點<br>
if L<size and array[L]>array[i]: MAX = L <br>
比較i和L這兩個位置的數字哪個比較大，如果L這個位置的數字比較大，那這時MAX會變成L<br>
if R<size and array[R]>array[MAX]: MAX=R <br>
這時換R和MAX比較，如果R這個位置的數字比較大，那這時MAX會變成R <br>
if MAX != i: (如果MAX還是=i，那就不需要swap)<br>
self.swap(array,i,MAX) 當MAX不=i時，MAX和i交換<br>
self.heapify(array,MAX,size) 而這時以MAX這個位置為父節點，再比較三節點一次<br>
<br>
<br>
### heap_sort
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/def_heap_sort.jpg)
p = (size//2)-1 代表最後一個父節點的位置<br>
for k in range(p,-1,-1): self.heapify(nums,k,size)<br>
遞減迴圈，中間寫-1，代表跑到0才會停止<br>
後面還要再呼叫heapify，因為要從第一個root比到最後一個的root為止，流程圖有解釋<br>
這邊跑完代表這時已經是一個MAX Heap了<br>
end = size-1<br>
while(end > 0):<br>
self.swap(nums,0, end) 交換第一個(最大的root)和最後一個數字(最後但不一定是最小的leaf)<br>
self.heapify(nums,0,end)<br>
這邊這邊把最大的數字排進output的最後一個位置，再heapify一次變成MAX Heap<br>
end = end-1遞減迴圈，當位置都排完時，end會==0，這時迴圈就會停止<br>
<br>
<br>
<br>

以下的重點是如何creat a MAX Heap<br>
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/Heapify.png)

<br>
<br>
<br>

以下流程圖省略每次Heapify的過程，重點在於如何sort<br>
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HeapSort.png)

![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HeapSort2.png)
 
參考資料<br>
-
ref = https://github.com/minsuk-heo/problemsolving/blob/master/sort/HeapSort.py
