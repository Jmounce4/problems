class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        for i in range(1, n):
            sqrd = ((2**i)-1)
            if sqrd >= n:
                return sqrd
