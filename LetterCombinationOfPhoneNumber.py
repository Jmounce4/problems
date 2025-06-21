class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        myList = []
        numberLetters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []

        def helpFunction(current, currentString):
                
            if current > len(digits)-1:
                myList.append(currentString)
                return
            for letter in numberLetters[digits[current]]:

                helpFunction(current+1, currentString+letter)

        helpFunction(0, "")
        return myList
