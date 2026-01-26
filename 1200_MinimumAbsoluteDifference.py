class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        minDiff = arr[len(arr)-1]
        returnArr = []

        if len(arr) < 3:
            returnArr.append([arr[0], arr[1]])

        for i in range(len(arr)-1):
            currentDiff = arr[i+1] - arr[i]
            
            if currentDiff == minDiff:
                returnArr.append([arr[i], arr[i+1]])
                minDiff = currentDiff

            if currentDiff < minDiff:
                returnArr = []
                minDiff = currentDiff
                returnArr.append([arr[i], arr[i+1]])
            
            
        
        return returnArr
