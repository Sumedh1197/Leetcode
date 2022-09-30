class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Time Complexity: O(n log n)
        
        #Creating Dictionary 
        ordered_map=dict()
        #Iterating over nums and adding values based on occurence of each number    
        for i in range(len(nums)):
            if ordered_map.has_key(nums[i]):
                ordered_map[nums[i]]+=1
            else:
                ordered_map[nums[i]]=1
        #Using sorted to extract sorted keys from dict based on value
        ordered_list= sorted(ordered_map,key=ordered_map.get,reverse=True)
        
        #Selecting top k from list and appending to resulting list 
        result=[]
        for i in range(len(ordered_list)):
            if i<k:
                result.append(ordered_list[i])
            else:
                break
        return result
        
        
        