#!/usr/bin/env python
# coding: utf-8

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
        


# In[2]:


output = Solution().merge_sort([3,2,-4,6,4,2,19])
output

