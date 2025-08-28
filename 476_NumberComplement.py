class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = (bin(num))[2:]
        complement = ''

        for i in range(len(binary)):
            if binary[i] == '0':
                complement += '1'
            else:
                complement += '0'

        return int(complement, 2)
