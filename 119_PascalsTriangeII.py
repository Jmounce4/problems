class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
       
        if rowIndex == 0:
            return [1]

        
        pascalArray = []
        for i in range(0, rowIndex+1):
            tempArray = []
            pascalArray.append([1])
            
            for j in range(1, len(pascalArray[i-1])):
                
                
                tempNum1 = pascalArray[i-1][j-1] 
                tempNum2 = pascalArray[i-1][j]
                pascalArray[i].append(tempNum1 + tempNum2)
            if i > 0:
                pascalArray[i].append(1)
            
            tempArray = pascalArray[i]
                #for j, add pascalArray[i-1][j-1] and pascalArray[i-1][j]


        return tempArray
