class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary1 = (bin(x))[2:]
        binary2 = (bin(y))[2:]
        while len(binary1) != len(binary2):
            if len(binary1) > len(binary2):
                binary2 = "0"+binary2
            else:
                binary1 = "0"+binary1

        counter = 0
        for i in range(len(binary1)):

            if binary1[i] != binary2[i]:
                counter+=1

        

        return counter
