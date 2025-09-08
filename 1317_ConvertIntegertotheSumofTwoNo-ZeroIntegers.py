class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num1 = 0
        num2 = 0
        myArray = []
        

        for i in range(1, n):
            num1 = i
            num2 = n - i
            if "0" in str(num1) or "0" in str(num2):
                continue
            else:
                myArray.append(num1)
                myArray.append(num2)
                return myArray


        
        return myArray
