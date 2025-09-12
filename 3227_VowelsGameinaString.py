class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """


        #Alice should insta win if ODD
        #Alice should grab odd ALL-1 if even, Bob grabs 0,  Alice grabs 1 and wins
        #Bob only wins with 0 vowels?
        ASCIIarray = set('AEIOUaeiou')
        vowelArray = []

        for i in range(len(s)):
            
            if s[i] in ASCIIarray:
                vowelArray.append(s[i])
        
        if len(vowelArray) > 0:
            return True
        else:
            return False



            #Simpler solution:
            ASCIIarray = set('AEIOUaeiou')

            for i in range(len(s)):
            
            if s[i] in ASCIIarray:
                return True
        
            return False
