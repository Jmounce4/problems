class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        numStr = str(num)
        maxStr = str(num)
        minStr = str(num)
        minDone = False
        maxDone = False

        for digit in numStr:
            digit_int = int(digit)
            if digit_int > 0:
                if not minDone:
                    minStr = minStr.replace(digit, '0')
                    minDone = True
            if digit_int < 9:
                if not maxDone:
                    maxStr = maxStr.replace(digit, '9')
                    maxDone = True
            
        maxNum = int(maxStr)
        minNum = int(minStr)
        return maxNum - minNum
