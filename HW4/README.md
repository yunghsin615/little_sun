Hash Table
-
Array+Linked-List為基礎的演算法<br>
首先，將文字或數字用一個經過Hash Function加密轉換成一串數字或一串有英文和數字的密碼<br>
那個函式是可以自己設計的，但這個作業我們使用現成的MD5來加密<br>
也因為MD5的關係，先將測值轉換成十六進位，再用int變成十進位，密碼就會變成純數字了！而且同一段文字每次出來的結果會相同<br>
再來，我的作法是將這個密碼除以要幾個抽屜，再取餘數，代表它該放進幾號抽屜<br>
如果函式處理得好，每個抽屜放一個東西的狀態是最好的<br>
如果有兩個密碼要放進同一個抽屜的事情發生，這叫做"碰撞"<br>
最後，最重要的就是要用Linked-List的方法將這些node串聯起來<br>
<br>
Hash Function(雜湊函式)<br>
這是加密過程要經歷的過程，它將複雜的文字透過函式轉換成密碼<br>
用甚麼國家的語言都可以，但要讓他知道是用甚麼編碼，像中文就是用utf-8<br>
老師說這是國際通用的，各個國家互相決定的編碼<br>
如果設計符合狀態的函式，最好的結果式每個抽屜只有一個東西<br>
這樣remove、contains花費的時間就會比較少，因為找到抽屜，然後抽屜裡有東西，就代表找到值了<br>
![image](https://github.com/yunghsin615/little_sun/blob/master/CodeSignal/Python/HashTable.jpg)
