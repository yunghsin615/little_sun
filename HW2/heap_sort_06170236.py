#!/usr/bin/env python
# coding: utf-8

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


# In[2]:


output = Solution().heap_sort([3,2,-4,6,4,2,19])
output

