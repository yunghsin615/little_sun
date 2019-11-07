# MergeSort / HeapSort 之比較
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/比較.jpg)

## MergeSort
### 時間複雜度:<br>
分割完變成一個一個單位，這是logn，一個一個排進array內，這是n<br>
所以ans:nlogn<br>
<br>
### 空間複雜度:
需要一個與原來List一樣的額外空間，來暫儲每一次分裂完的合併結果(Extra-Place)<br>
所以ans:O(n)<br>
<br>
### 穩定度:
最後因為分割->比較->合併，沒有像QuickSort有選pivot的運氣成分<br>
所以穩定度是成穩定的<br>
<br>
<br>
## HeapSort
### 時間複雜度:<br>
建立MAX Heap時是n，執行n-1次的sort是(n-1) × Ο(log n) = Ο( n log n)<br>
算式 = Ο(n) + Ο( n log n) = Ο( n log n)<br>
所以ans:nlogn<br>
### 空間複雜度:
我們都以二元數的方式思考，但它只有在原來的list裡面交換而已(In-Place)<br>
所以ans:O(1)
### 穩定度:
因為有排序的問題，如果input本身就剛好是MAX Heap，那根本不用Heapify，可以直接heap_sort<br>
所以穩定度是成不穩定的<br>
<br>
<br>
參考資料<br>
1:https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-%E6%BC%94%E7%AE%97%E6%B3%95%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%95%B4%E7%90%86<br>
2:http://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php<br>
