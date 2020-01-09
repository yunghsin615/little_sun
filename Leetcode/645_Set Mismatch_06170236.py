class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup = 0
        missing = 0
        
        for i in range(1,len(nums)+1):
            count = 0
            for j in range(0,len(nums)):
                if nums[j] == i :
                    count = count+1          
            if count == 2 :
                dup = i
            elif count == 0 :
                missing = i
                    
        return[dup,missing]
    
    
    
