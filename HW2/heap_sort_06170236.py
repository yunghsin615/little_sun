#!/usr/bin/env python
# coding: utf-8

# 結果
# -
# 先把最後的程式碼show出來，不然我怕我寫太亂，助教頭昏眼花(ˊ･ω･ˋ)

# In[1]:


class Solution(object):
    
    def heap_sort(self, nums):
        size=len(nums)
        p = (size//2)-1 #最後一個父節點的位置
        for k in range(p,-1,-1): #遞減迴圈，中間要寫-1，才會跑到0為止
            self.heapify(nums,k,size)

        end = size-1
        while(end > 0):
            self.swap(nums,0, end)
            self.heapify(nums,0,end)
            end = end-1

        return nums


    def swap(self,array,i,j): #定義如何互換
        array[i],array[j]= array[j],array[i]

    def heapify(self,array,i,size): #定義MAX化的過程
        MAX = i
        L,R = i*2+1,i*2+2 #L=左節點,R=右節點
        if L<size and array[L]>array[i]: #先找到i,L,R裡面最大的那個，然後把它放在root的位子
            MAX = L                      #多加條件式L<size，

        if R<size and array[R]>array[MAX]:
            MAX = R

        if MAX != i: #如果MAX還是=i，那就不需要swap
            self.swap(array,i,MAX)
            self.heapify(array,MAX,size)

            
output = Solution().heap_sort([3,2,-4,6,4,2,19])
output


# 2019/11/3<br>
# 在看影片的時候覺得只要子節點比父節點大就會交換<br>
# 交換這個動作很簡單，可是應該會很常用到，所以先給他一個def<br>

# In[ ]:


def swap(i,j): #先定義如何互換
    array[i],array[j]= array[j],array[i]

def heapify(leaf,i): #MAX化的過程
    top = i
    L,R = i*2+1,i*2+2  #L=左節點,R=右節點
    if array[L]>array[i]:  #這邊只要子節點比父節點大就直接交換
        swap(i,L)
        
    if array[R]>array[i]:
        swap(i,R)


# 2019/11/5<br>
# 後來才發現上述這樣做是沒有效率的，應該把三節點比較完，再把最大的那個放root<br>

# In[45]:


def swap(i,j): #先定義如何互換
    array[i],array[j]= array[j],array[i]

def heapify(array,i): #定義MAX化的過程
    MAX = i
    L,R = i*2+1,i*2+2  #L=左節點,R=右節點
    
    #先找到i,L,R裡面最大的那個，然後把它放在父節點的位子
    if array[L]>array[i]:  
        MAX = L
        
    if array[R]>array[MAX]:
        MAX = R
        
    if MAX != i: #如果MAX還是=i，那就不需要swap
        swap(MAX,i)
        heapify(MAX,len(array))
        


# 由下面這個例子來看<br>
# 就算把i跟j交換了，i的位置還是沒有變，不會因為交換了數字就把位置改了<br>
# i還是在0，不過這個index位置的數字從2變成3

# In[46]:


array=[2,3]
swap(0,1)
print(array)
print(i)
print(array[i])


# 寫了一個迴圈從0到最後，試試看每個位置都比較過，還是一個大失敗(´༎ຶД༎ຶ )<br>

# In[47]:


def heap_sort(array):  
    for k in range(0,len(array)):
        heapify(array,k)

def swap(i,j): #先定義如何互換
    array[i],array[j]= array[j],array[i]

def heapify(array,i): #定義MAX化的過程
    MAX = i
    L,R = i*2+1,i*2+2 #L=左節點,R=右節點
    if array[L]>array[i]: #先找到i,L,R裡面最大的那個，然後把它放在root的位子
        MAX = L

    if array[R]>array[MAX]:
        MAX = R

    if MAX != i: #如果MAX還是=i，那就不需要swap
        swap(MAX,i)
        heapify(array,MAX)

    
arr=[21,15,30,6,12,25,7,19,26]
heap_sort(arr)
print(arr)


# 2019/11/6<br>
# 看了一個影片的解釋後，還是不知如何寫下程式碼，就查了他的<br>
# ref = https://github.com/minsuk-heo/problemsolving/blob/master/sort/HeapSort.py<br>

# In[4]:


def heap_sort(array):
    
    size=len(array)
    p = (size//2)-1 #這個很重要，p是最後一個父節點的位置
    for k in range(p,0,-1): #遞減迴圈
        heapify(array, k,size)
        
    #下面這段是    
    end = size-1
    while(end > 0):
        swap(array,0, end)
        heapify(array,0,end)
        end = end-1

    return array
    
def swap(array,i,j): #定義如何互換
    array[i],array[j]= array[j],array[i]

def heapify(array,i,size): #定義MAX化的過程
    MAX = i
    L,R = i*2+1,i*2+2 #L=左節點,R=右節點
    
    #先找到i,L,R裡面最大的那個，然後把它放在root的位子
    if array[L]>array[i]: 
        MAX = L                      

    if array[R]>array[MAX]:
        MAX = R

    if MAX != i: #如果MAX還是=i，那就不需要swap
        swap(array,i,MAX)
        heapify(array,MAX,size)
        
  
       
arr=[2,5,1,4]
heap_sort(arr)


# In[3]:


def heap_sort(array):
    
    size=len(array)
    p = (size//2)-1 #這個很重要，p是最後一個父節點的位置
    for k in range(p,-1,-1): #遞減迴圈，中間要寫-1，才會跑到0為止
        heapify(array,k,size)
        
    end = size-1
    while(end > 0):
        swap(array,0, end)
        heapify(array,0,end)
        end = end-1

    return array
    
def swap(array,i,j): #定義如何互換
    array[i],array[j]= array[j],array[i]

def heapify(array,i,size): #定義MAX化的過程
    MAX = i
    L,R = i*2+1,i*2+2 #L=左節點,R=右節點
    if L<size and array[L]>array[i]: #先找到i,L,R裡面最大的那個，然後把它放在root的位子
        MAX = L                      ##多加條件式L<size，

    if R<size and array[R]>array[MAX]:
        MAX = R                      ##多加條件式R<size

    if MAX != i: #如果MAX還是=i，那就不需要swap
        swap(array,i,MAX)
        heapify(array,MAX,size)


    
        
arr=[21,15,30,6,12,25,7,19,26]
heap_sort(arr)


# 以下是套入助教規定的格式中:)<br>

# In[2]:


class Solution(object):
    def heap_sort(self, nums):

        size=len(nums)
        p = (size//2)-1
        for k in range(p,-1,-1): #遞減迴圈，中間要寫-1，才會跑到0為止
            self.heapify(nums,k,size)

        end = size-1
        while(end > 0):
            self.swap(nums,0, end)
            self.heapify(nums,0,end)
            end = end-1

        return nums


    def swap(self,array,i,j): #定義如何互換
        array[i],array[j]= array[j],array[i]

    def heapify(self,array,i,size): #定義MAX化的過程
        MAX = i
        L,R = i*2+1,i*2+2 #L=左節點,R=右節點
        if L<size and array[L]>array[i]: #先找到i,L,R裡面最大的那個，然後把它放在root的位子
            MAX = L                      #多加條件式L<size，

        if R<size and array[R]>array[MAX]:
            MAX = R

        if MAX != i: #如果MAX還是=i，那就不需要swap
            self.swap(array,i,MAX)
            self.heapify(array,MAX,size)

            
output = Solution().heap_sort([3,2,-4,6,4,2,19])
output

