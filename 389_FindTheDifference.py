class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sortedT = sorted(t)
        sortedS = sorted(s)

        for i in range(len(sortedT)):
            if i >= len(sortedS):
                return sortedT[i]
            if sortedT[i] != sortedS[i]:
                return sortedT[i]
