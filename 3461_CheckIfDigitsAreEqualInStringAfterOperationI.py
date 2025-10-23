class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = [int(c) for c in s]

        while(len(s) > 2):
            newS = []
            for i in range(len(s)-1):
                current = ((s[i]) + (s[i+1])) % 10
                
                newS.append(current)

            s = newS

        return s[0] == s[1]

