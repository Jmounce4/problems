class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return False
        if n % 2 == 0:
            return True
        if n % 2 != 0:
            return False
