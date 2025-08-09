class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        sum = n
        while sum > 9 or sum == 7:
            digits_list = list(map(int, str(sum)))
            newSum = 0
            for digit in digits_list:
                newSum += (digit*digit)
            
            sum = newSum



        if sum > 1:
            return False
        else:
            return True
