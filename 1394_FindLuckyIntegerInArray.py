class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #add each number to dictionary and increment frequency

        myDict = {}
        arr.sort()
        lucky = -1
        for i in range(len(arr)):
            if arr[i] not in myDict:
                myDict[arr[i]] = 1
            else:
                myDict[arr[i]] += 1


        for key in myDict:
            if key == myDict[key]:
                lucky = key

        
        return lucky
