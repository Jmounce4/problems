class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        if num > 9:
            return (num-1)%9+1
        else:
            return num
    
