class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Time Complexity: O(n)
    
        #Initializing max value
        max_val= 0 
        #Left and right pointer
        left= 0
        right= len(height)-1
        
        while(left<right):
            #Finding product of current pointers 
            current_volume= (right-left) * min(height[left],height[right])
            
            if current_volume>max_val:
                max_val=current_volume
            #Increment/Decrement counter of the pointer with a smaller value
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return max_val
        