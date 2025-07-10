class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        
        pascalArray = []
        tempArray = []
        for i in range(0, numRows):
            pascalArray.append([1])
            for j in range(1, len(pascalArray[i-1])):

                tempNum1 = pascalArray[i-1][j-1] 
                tempNum2 = pascalArray[i-1][j]
                pascalArray[i].append(tempNum1 + tempNum2)

            if i > 0:
                pascalArray[i].append(1)

                #for j, add pascalArray[i-1][j-1] and pascalArray[i-1][j]


        return pascalArray
