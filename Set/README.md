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
