#!/usr/bin/env python
# coding: utf-8

# 結果
# -
# 先把最後的程式碼show出來，不然我怕我寫太亂，助教頭昏眼花(ˊ･ω･ˋ)

# In[1]:


class Solution(object):
    def merge_sort(self,nums):

        if len(nums) > 1 :
            middle = int (len(nums)/2) #有可能是奇數，所以用int
            left=self.merge_sort(nums[:middle]) #:擺在middle前面

            right=self.merge_sort(nums[middle:]) #:擺在middle後面

            return self.Merge(left,right) 

        else:
            return nums


    def Merge(self,A,B):
        i = 0
        j = 0
        C=[]
        while (i<len(A) and j<len(B)):  
            if(A[i]<=B[j]):
                C.append(A[i])
                i=i+1

            elif(A[i]>B[j]):
                C.append(B[j])
                j=j+1

        #某邊的值空了，另一邊剩下來的值要加到C裡面
        while (i==len(A) or j==len(B)):
            if(i == len(A)):   #i==len(A)表示A空了
                C.append(B[j]) #再把B[j]這個數字加進C
                j=j+1          #可能剩下的不只一個數字，所以還要+1，再繼續跑迴圈

            elif(j == len(B)):
                C.append(A[i])
                i=i+1

            while(i==len(A) and j==len(B)): #!!!這邊很重要!!!最後i==(A)而j也==len(B)時，迴圈就會一直跑，不會終止，所以設這個停止條件式

                return C
        
output = Solution().merge_sort([3,2,-4,6,4,2,19])
output


# 2019/10/27<br>
# 一開始想說有兩兩比較，而且都要從頭走到尾走訪一遍，那是不是有兩個迴圈呢?<br>
# 可是要怎麼樣把兩個寫在一起?雖然很顯然的不會是並排，然後兩層的邏輯也不太對，但還是把學習歷程留下來了(´･Д･)」<br>

# In[2]:


A=[1,3,5,9]
B=[2,7,8,10]
C=[]
for i in range(0,len(A)):
for j in range(0,len(B)):
    if A[i]<B[j]:
        C.append(A[i])
        i=i+1
    elif A[i]>=B[j]:
        C.append(B[j])


# In[3]:


A=[1,3,5,9]
B=[2,7,8,10]
C=[]
for i in range(0,len(A)):
    for j in range(0,len(B)):
        if A[i]<B[j]:
            C.append(A[i])
            break
        elif A[i]>=B[j]:
            C.append(B[j])
print(C)


# 2019/10/29<br>
# 今天上完老師的課，換了一個想法，不一定要用迴圈，C=[0]*(len(A)+len(B))，再把比較完的數字替換掉0<br>
# 然後不出乎意料的又失敗了(´༎ຶД༎ຶ )，沒辦法執行出結果<br>

# In[4]:


def Merge(A,B,C,i,j,m):
    
    if(A[i]<=B[j]):
        C[m]=A[i]
        i=i+1
        m=m+1
    elif(A[i]>B[j]):
        C[m]=B[j]
        j=j+1
        m=m+1
    
        print(C) 
    
A=[1,3,5,9]
B=[2,7,8,10]
C=[0]*(len(A)+len(B))
i = 0
j = 0
m = 0
Merge(A,B,C,i,j,m)


# 2019/10/30<br>
# 查了一下迴圈除了for之外，還有while迴圈，用法的差別在於for適用於已知迴圈數，而while適用於無法預知迴圈數<br>
# 當程式需要不斷地重覆某些運算，一直到出現指定的特殊狀況時才停止，這種情形就比較適合用 while-loop 來實現。<br>
# ref1 = https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-4990a5757aa6<br>
# 雖然有辦法寫else的註解，可是自己也覺得怪怪的<br>

# In[5]:


def Merge(A,B):
    i = 0
    j = 0
    C=[]
    while 1:  #判斷條件值為1, 代表迴圈永遠成立(這是ref1裡面的說明)
        if(A[i]<=B[j]):
            C.append(A[i])
            i=i+1

        elif(A[i]>B[j]):
            C.append(B[j])
            j=j+1
            
        else: #某邊的值空了，另一邊剩下來的值要加到C裡面
            if(i == len(A)):   #A的9加入C之後，i=i+1=4，len(A)=4，所以這邊寫==，這行是A陣列空掉的條件式
                C.append(B[j]) #A陣列空了，所以把B陣列的值加入C
                j=j+1          #有可能不只多一個值，所以要再+1
            elif(j == len(B)): 
                C.append(A[i])
                i=i+1
           
    return C

A=[1,3,5,9]
B=[2,7,8,10]
Merge(A,B)


# 下面是以C陣列裡都是0，再把A和B每個數字替換掉0<br>
# 以error來看，上下兩個方法都錯在同個地方<br>

# In[6]:


def Merge(A,B):
    i = 0
    j = 0
    m = 0
    C=[0]*(len(A)+len(B))
    
    while 1:  #判斷條件值為1, 代表迴圈永遠成立(這是參考資料的說明)
        if(A[i]<=B[j]):
            C[m]=A[i] #把C那個位置的0替換為A[i]
            i=i+1
            m=m+1

        elif(A[i]>B[j]):
            C[m]=B[j] #把C那個位置的0替換為B[j]
            j=j+1
            m=m+1
            
        else:
            if(i>=len(A)):
                C[m] = B[j]
            elif(j>=len(B)):
                C[m] = A[i]

    return C

A=[1,3,5,9]
B=[2,7,8,10]
Merge(A,B)


# 原來是while條件式的部分阿<br>
# <br>
# 2019/11/2<br>
# 寫完merge_Sort再回來看，發現少了最後一個數字<br>

# In[7]:


def Merge(A,B):
    i = 0
    j = 0
    C=[]
    while i<len(A) and j<len(B):  #迴圈不能用while1:，還是要有範圍
        if(A[i]<=B[j]):
            C.append(A[i])
            i=i+1

        elif(A[i]>B[j]):
            C.append(B[j])
            j=j+1
            
        else: #某邊的值空了，另一邊剩下來的值要加到C裡面
            if(i == len(A)):   #A的9加入C之後，i=i+1=4，len(A)=4，所以這邊寫==，這行是A陣列空掉的條件式
                C.append(B[j]) #A陣列空了，所以把B陣列的值加入C
                j=j+1          #有可能不只多一個值，所以要再+1
            elif(j == len(B)): 
                C.append(A[i])
                i=i+1
           
    return C

A=[1,3,5,9]
B=[2,7,8,10]
Merge(A,B)


# 2019/11/1<br>
# 現在要開始merge_sort的部分<br>
# 這個是以psuedocode寫出來的，但是這不是python的寫法<br>

# In[8]:


def merge_sort(A,p,r):
    if(p<r):
        middle = int (r/2)
        merge_sort(A, p, middle)
        merge_sort(A, middle+1, r)
        Merge(A,p,middle,r)
        


# 2019/11/2<br>
# 最後還是上網查了<br>
# ref2 = https://yunlinsong.blogspot.com/2017/05/python.html　

# In[9]:


def Merge_Sort(a):
    
    if len(a) > 1 :
        middle = int (len(a)/2) #有可能是奇數，所以用int
        left=Merge_Sort(a[:middle]) #:擺在middle前面

        right=Merge_Sort(a[middle:]) #:擺在middle後面

        return Merge(left,right) #看了很久不知哪裡錯了，結果原來是Merge寫錯!!!
        
    else:
        return a

a=[2,4,6,1,3,6]
Merge_Sort(a)


# In[10]:


def Merge(A,B):
    i = 0
    j = 0
    C=[]
    while (i<len(A) and j<len(B)): #迴圈不能用while1:，還是要有範圍
        if(A[i]<=B[j]):
            C.append(A[i])
            i=i+1

        elif(A[i]>B[j]):
            C.append(B[j])
            j=j+1
            
    #某邊的值空了，另一邊剩下來的值要加到C裡面，這邊是參考ref2對於merge_sort那部分的概念
    if(i == len(A)):
        C = C + B[j:] #當i==A長度時，代表A空了，所以把B剩下的值加入C
    elif(j == len(B)):
        C = C + A[i:] #當j==B長度時，代表B空了，所以把A剩下的值加入C


    return C

A=[1,3,5,9]
B=[2,7,8,10]
Merge(A,B)


# 最後就是把他們寫在一起!雖然不是所有都是我自己想的<br>
# 但最後結果出來還是好感動ಥ_ಥ<br>

# In[11]:


def Merge_Sort(a):
    
    if len(a) > 1 :
        middle = int (len(a)/2) #有可能是奇數，所以用int
        left=Merge_Sort(a[:middle]) #:擺在middle前面

        right=Merge_Sort(a[middle:]) #:擺在middle後面

        return Merge(left,right) 
        
    else:
        return a


def Merge(A,B):
    i = 0
    j = 0
    C=[]
    while (i<len(A) and j<len(B)):  
        if(A[i]<=B[j]):
            C.append(A[i])
            i=i+1

        elif(A[i]>B[j]):
            C.append(B[j])
            j=j+1
            
    #某邊的值空了，另一邊剩下來的值要加到C裡面
    if(i == len(A)):
        C = C + B[j:] #當i==A長度時，代表A空了，所以把B剩下的值加入C
    elif(j == len(B)):
        C = C + A[i:] #當j==B長度時，代表B空了，所以把A剩下的值加入C


    return C

a=[4,6,2,8,1,100,2,4,36,84,22]
Merge_Sort(a)


# 2019/11/5<br>
# 現在要把這些程式碼再寫進助教的格式內<br>

# In[12]:


class Solution(object):
    def merge_sort(self,nums):

        if len(nums) > 1 :
            middle = int (len(nums)/2) #有可能是奇數，所以用int
            left=self.merge_sort(nums[:middle]) #:擺在middle前面

            right=self.merge_sort(nums[middle:]) #:擺在middle後面

            return self.Merge(left,right) 

        else:
            return nums


    def Merge(self,A,B):
        i = 0
        j = 0
        C=[]
        while (i<len(A) and j<len(B)):  
            if(A[i]<=B[j]):
                C.append(A[i])
                i=i+1

            elif(A[i]>B[j]):
                C.append(B[j])
                j=j+1

        #某邊的值空了，另一邊剩下來的值要加到C裡面
        if(i == len(A)):
            C = C + B[j:] #當i=A長度時，代表A空了，所以把B剩下的值加入C
        elif(j == len(B)):
            C = C + A[i:] #當j=B長度時，代表B空了，所以把A剩下的值加入C


        return C

output = Solution().merge_sort([3,2,-4,6,4,2,19])
output


# 2019/11/6<br>
# 前面的[:]的概念不是自己的，雖然前面結果已經出來了<br>
# 但我想說可以用自己的想法試試看<br>

# In[13]:


def Merge_Sort(a):
    
    if len(a) > 1 :
        middle = int (len(a)/2) #有可能是奇數，所以用int
        left=Merge_Sort(a[:middle]) #:擺在middle前面

        right=Merge_Sort(a[middle:]) #:擺在middle後面

        return Merge(left,right) 
        
    else:
        return a


def Merge(A,B):
    i = 0
    j = 0
    C=[]
    while (i<len(A) and j<len(B)):  
        if(A[i]<=B[j]):
            C.append(A[i])
            i=i+1

        elif(A[i]>B[j]):
            C.append(B[j])
            j=j+1
            
    #某邊的值空了，另一邊剩下來的值要加到C裡面
    while (i==len(A) or j==len(B)):
        if(i == len(A)):   #i==len(A)表示A空了
            C.append(B[j]) #再把B[j]這個數字加進C
            j=j+1          #可能剩下的不只一個數字，所以還要+1，再繼續跑迴圈

        elif(j == len(B)):
            C.append(A[i])
            i=i+1
            
        return C
          
a=[3,2,-4,6,4,2,19]
Merge_Sort(a)


# 2019/11/7<br>
# 因為while (i==len(A) or j==len(B)):這個條件式會一直成立，所以要設個停止點<br>
# 太好了，終於搞清楚哪裡錯了，感動到痛苦流涕ಥ_ಥ

# In[14]:


def Merge_Sort(a):
    
    if len(a) > 1 :
        middle = int (len(a)/2) #有可能是奇數，所以用int
        left=Merge_Sort(a[:middle]) #:擺在middle前面

        right=Merge_Sort(a[middle:]) #:擺在middle後面

        return Merge(left,right) 
        
    else:
        return a


def Merge(A,B):
    i = 0
    j = 0
    C=[]
    while (i<len(A) and j<len(B)):  
        if(A[i]<=B[j]):
            C.append(A[i])
            i=i+1

        elif(A[i]>B[j]):
            C.append(B[j])
            j=j+1
            
    #某邊的值空了，另一邊剩下來的值要加到C裡面
    while (i==len(A) or j==len(B)):
        if(i == len(A)):   #i==len(A)表示A空了
            C.append(B[j]) #再把B[j]這個數字加進C
            j=j+1          #可能剩下的不只一個數字，所以還要+1，再繼續跑迴圈
            
        elif(j == len(B)):
            C.append(A[i])
            i=i+1
            
        while(i==len(A) and j==len(B)): #!!!這邊很重要!!!最後i==(A)而j也==len(B)時，上個迴圈就會一直跑，不會終止，所以設這個停止條件式

            return C
          
a=[3,2,-4,6,4,2,19]
Merge_Sort(a)

