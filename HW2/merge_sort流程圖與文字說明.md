# MergeSort

Time Complexity = Nlog^N<br>
每次都把一個數列分為兩堆，直到剩下1個為止，不像QuickSort會有選pivot的運氣問題，而是成穩定的時間狀態<br>
一個數字和一個數字比較後合併成兩個數字的數列，兩個數字和兩個數字比較後合併成四個數字的數列...以此類推<br>
一層一層合併到變成原本的長度就結束了，然後這時數字要是按照排列的<br>
我會把它拆解成兩個部分來看，第一部分是**sort**，分堆後比大小的過程<br>
第二部分是**merge**，比完大小並把他們匯集成同個陣列的過程<br>
其實雖然說是拆成兩個部分來看，但它們的意義沒有完全被分開<br>
<br>
<br>
### merge_sort<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/def_merge_sort.jpg)
帶入我的流程圖做解釋，middle = int (len(nums)/2)=4<br>
left=self.merge_sort(nums[:middle])  冒號在前面代表沒有包含這個位置(0-3)的前面的值<br>
right=self.merge_sort(nums[middle:]) 冒號在後面代表有包含這個位置(4-7)的後面的值<br>
全部分完變成一個一個後，再呼叫Merge<br>
<br>
### Merge<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/def_Merge.jpg)
while (i<len(A) and j<len(B)): 比較小的那個append到空陣列C裡面<br>
while (i==len(A) or j==len(B)): 當滿足其中一個條件時，代表那個陣列已經空了<br>
if(i == len(A)): 代表A陣列已經空了
C.append(B[j]) 把B[j]這個數字加進C
j=j+1   可能剩下的不只一個數字，所以還要+1，再繼續跑迴圈
但如果只有這樣的話，j遲早會==(B)，迴圈會一直被滿足，不會停止<br>
**while(i==len(A) and j==len(B))** !!!這句很重要，代表一個停止條件式<br>
<br>

以下是流程圖<br>
-
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/MergeSort.png)

參考資料<br>
-
ref1 = https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-4990a5757aa6<br>
ref2 = https://yunlinsong.blogspot.com/2017/05/python.html　
