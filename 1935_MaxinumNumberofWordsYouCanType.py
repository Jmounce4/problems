class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        currentString = ''
        total = 0
        checker = 0
        for i in text:
            

            if i == ' ':
                if checker == 0:
                    total += 1
                else:
                    checker = 0
                currentString = ''
                continue

            if i in brokenLetters:
                checker+=1
        
        if checker == 0:
            total+=1
            
        return total
