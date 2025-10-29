class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        temp = [i for i in score]
        temp.sort(reverse=True)
        myDict = {}
        for i in range(len(temp)):
            if i == 0:
                scoring = "Gold Medal"
            elif i == 1:
                scoring = "Silver Medal"
            elif i == 2:
                scoring = "Bronze Medal"
            else:
                scoring = str(i+1)
            
            myDict[temp[i]] = scoring

        finalArray = []
        for i in score:
            if i in myDict:
                finalArray.append(myDict[i])

        return finalArray
