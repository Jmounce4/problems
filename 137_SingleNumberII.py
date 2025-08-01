class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        myDict = {}

        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] += 1

        
        for i in myDict:
            if myDict[i] == 1:
                return i
