class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelArray = []
        
        ASCIIarray = set('AEIOUaeiou')

        for i in range(len(s)):
            
            if s[i] in ASCIIarray:
                vowelArray.append(s[i])
        
        vowelArray.sort()
        newString = []
        counter = 0 
        for j in range(len(s)):
            
            if s[j] in ASCIIarray:
                newString.append(vowelArray[counter])
                counter+=1
            else:
                newString.append(s[j])
        return ''.join(newString)
