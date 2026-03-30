class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        evens = []
        evens2 = []
        odds = []
        odds2 = []
        for i in range(len(s1)):
            if i % 2 == 0:
                evens.append(s1[i])
                evens2.append(s2[i])
            else:
                odds.append(s1[i])
                odds2.append(s2[i])
        
        return(
            (sorted(evens) == sorted(evens2)) and
            (sorted(odds) == sorted(odds2))
        )
