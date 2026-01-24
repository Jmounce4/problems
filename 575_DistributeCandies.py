class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        counter = 0
        candyDict = {}
        for i in candyType:
            if i not in candyDict:
                counter+=1
                candyDict[i] = 1
        
        if counter <= len(candyType)/2:
            return counter
        else:
            return len(candyType)/2
