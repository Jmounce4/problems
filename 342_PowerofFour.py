class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n > 4 and n % 4 == 0:
            n //= 4
        
        if n == 1 or n == 4:
            return True
        else:
            return False
