class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Time Complexity: O(s)+O(t) 
        #Create two dictionaries
        s_map= dict()
        t_map=dict()
        
        #Iterare over both strings and add each character in the 2 respective dictionaries
        
        #Iterating over String s
        for char1 in s:
            if s_map.has_key(char1):
                s_map[char1]+=1
            else:
                s_map[char1]=1
        
        #Iterating over String t 
        for char2 in t:
            if t_map.has_key(char2):
                t_map[char2]+=1
            else:
                t_map[char2]=1
        
        #Checking if both dictionaries are equal 
        if s_map==t_map:
            return True
        else:
            return False
    
            
        