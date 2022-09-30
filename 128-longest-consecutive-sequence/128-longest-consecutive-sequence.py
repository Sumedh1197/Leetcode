class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        #Time complexity: O(n)
        
        #Initialize the longest length to 0 
        longest_length=0
        #Create a set of given list to have distinct numbers
        nums=set(nums)
        
        for n in nums:
            #If a number has a consecutive neighbor smaller than it then skip else 
            # use this number as the starting point of the sequence 
            if (n-1) not in nums:
                length=1
                
                #Checking the number of consecutive numbers present for eahc starting point
                while (n+length) in nums:
                    length+=1
                #Getting max of longest length till now
                longest_length=max(length,longest_length)
                
        return longest_length
            
    
 
                
        