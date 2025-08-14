class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        triple = ''
        for i in range(len(num)-2):

            if num[i] == num[i+1] and num[i] == num[i+2]:
                newTriple = str(num[i])*3
                if newTriple > triple:
                    triple = newTriple

        return triple
