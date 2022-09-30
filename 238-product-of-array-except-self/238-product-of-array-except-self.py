class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Time Complexity: O(n) 
        result=[1]*len(nums)
        
        #Calculating prefix for each position i.e product of elements until that position
        prefix= 1
        for n in range(len(nums)):
            result[n]=prefix
            prefix*=nums[n]
        #Multiplying postfix values by prefix values to generate result array 
        postfix=1
        
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]
        
        return result
            
            
        