class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Time Complexity: O(n)
        #Generate clean string by converting to lowercase and only including alphanumeric char
        clean_string= ''.join(char.lower() for char in s if char.isalnum())
        
        #Initialize 2 points: left and right
        left=0
        right=len(clean_string)-1
        
        while(left<right):
            #If values at each end don't match quit!
            if clean_string[left]!=clean_string[right]:
                return False
            left+=1
            right-=1
        return True
        