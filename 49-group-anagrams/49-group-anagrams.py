class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        #Time Complexity: O(m.n.26) or O(m.n) where m is length of strs and n is avg length of each str
        #Create a defaultdict of list 
        
        result= defaultdict(list)
        
        for word in strs:
            count= [0]* 26 #Since we have 26 alphabets 
            
            for char in word:
                count[ord(char)-ord('a')]+=1 #Taking ASCII values and subtracting with 'a' to get correct index
            
            #Cannot append mutable object like list as key hence need to convert into tuple
            result[tuple(count)].append(word)
            
        #Returning values of the dictionary since we passed them as a list by default    
        return result.values()
        
        
                

          
                
                    
            