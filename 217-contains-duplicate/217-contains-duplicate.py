class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map_num= {}
        
        for i in range(len(nums)):
            if map_num.has_key(nums[i]):
                return True
            else:
                map_num[nums[i]]=1
            
        return False
        