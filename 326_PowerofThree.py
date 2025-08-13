class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n
        while temp > 3 and temp % 3 == 0:
            temp //= 3
        
        if temp == 1 or temp == 3:
            return True
        else:
            return False
