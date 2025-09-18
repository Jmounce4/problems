class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        end = len(digits)-1
        decrement = end
        carry = 0

        while digits[decrement] == 9 and decrement >= 0:
            digits[decrement] = 0
            decrement -= 1

        if decrement >= 0:
            digits[decrement] = digits[decrement]+1

        if decrement == -1:
            digits[0] = 1
            digits.append(0)

        return digits
