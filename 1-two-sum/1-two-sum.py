class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Time complexity O(n^2)
        
        #Iterate over the list, find the difference between each element and target
        #If the difference is present in the list, then return both the indices
        for idx,n in enumerate(nums):
            diff= target - n 
            if diff in nums and idx!=nums.index(diff):
                return [idx, nums.index(diff)]
        
        
        
        
        