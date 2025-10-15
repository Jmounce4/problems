class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        topStr = "qwertyuiop"
        midStr = "asdfghjkl"
        botStr = "zxcvbnm"

        top = 0
        mid = 0
        bot = 0

        finalStr = []

        for word in words:
            for j in range(len(word)):
                
                
                if word[0].lower() in topStr:
                    top = 1
                    

                if word[0].lower() in midStr:
                    mid = 1
                    

                if word[0].lower() in botStr:
                    bot = 1
                    

                if top == 1:
                    if word[j].lower() not in topStr:
                        break

                if mid == 1:
                    if word[j].lower() not in midStr:
                        break

                if bot == 1:
                    if word[j].lower() not in botStr:
                        break

                

                if j == len(word)-1:
                    finalStr.append(word)

            top = 0
            mid = 0
            bot = 0
        
        return finalStr
