class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        numStr = str(num)
        maxStr = str(num)
        minStr = str(num)
        minDone = False
        maxDone = False
        i = 0
        firstDigit = 0
        for digit in numStr:
            
            digit_int = int(digit)
            if i == 0 :
                firstDigit = digit_int
                if digit_int <= 9 and digit_int is not 1:
                    if not minDone:
                        minStr = minStr.replace(digit, '1')
                        minDone = True
                        
            else:
                if digit_int <= 9 and digit_int is not 0 and digit_int != firstDigit:
                    if not minDone:
                        minStr = minStr.replace(digit, '0')
                        minDone = True
            if digit_int < 9:
                if not maxDone:
                    maxStr = maxStr.replace(digit, '9')
                    maxDone = True
            i+=1
        maxNum = int(maxStr)
        minNum = int(minStr)
        return maxNum - minNum
