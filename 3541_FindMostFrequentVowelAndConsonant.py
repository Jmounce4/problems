class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set('aeiouAEIOU')
        vowelDict = {}
        consDict = {}


        for i in s:
            if i in vowels:
                if i in vowelDict:
                    vowelDict[i] += 1
                else:
                    vowelDict[i] = 1
            else:
                if i in consDict:
                    consDict[i] += 1
                else:
                    consDict[i] = 1

        maxVowels = 0
        maxCons = 0
        
        if len(vowelDict) > 0:
            maxVowels = max(vowelDict.values())
        if len(consDict) > 0:
            maxCons = max(consDict.values())

        return maxVowels + maxCons
