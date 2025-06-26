class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagramDict = {}

        for word in strs:
            key = ''
            sortedWord = sorted(word)
            for char in sortedWord:
                key += char
            if key not in anagramDict:
                anagramDict[key] = []
            anagramDict[key].append(word)

        return anagramDict.values()
