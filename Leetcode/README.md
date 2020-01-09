# Leetcode
### 9_Palindrome Number
輸入的數字從前到後跟從後到前是不是一樣的?<br>
首先，負數因為倒過來負號會在後面，所以不管數字怎樣，小於0一定都是錯的<br>
再來就是轉成字串，再把它倒過來，看看兩個有沒有相等<br>
<br>
### 27_Remove Element
當要刪除的數字在數列中，就刪除該數字，直到沒有那個數字了就結束迴圈
<br>
### 155_Min Stack
**push**把值加入array的最後一位，直接用append<br>
**pop**刪除最後加入的值，直接用pop<br>
**top**回傳最上方的盤子，是array的最後一個[-1]<br>
**getMin**定義一個sort是array從小排到大，再回傳第0位<br>
<br>
### 232_Implement Queue using Stacks
**push**把值加入array的最後一位，直接用append<br>
**pop**pop的用法是刪除位置，要刪除的是array的第一位，所以pop(0)<br>
**peek**回傳第一個位子的值array[0]<br>
**empty**檢查是否是空的，len(array)是否為0<br>
<br>
### 707_Design Linked List
**get**輸入index位子，得到該位子的值<br>
**addAtHead**將val加到第一位(self.head)<br>
**addAtTail**將val加到最後一位<br>
**addAtIndex**輸入index位子和val，在該位子加入val<br>
**deleteAtIndex**輸入index位子，刪除該位子的值<br>
<br>
