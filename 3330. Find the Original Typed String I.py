class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        possibleStrings = 1
        

        for i in range(len(word)-1):

            if word[i] == word[i+1]:
                possibleStrings+=1
                
        return possibleStrings
