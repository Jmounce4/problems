class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myDict = {}
        count = 0
        maxFreq = 0

        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1

            if myDict[i] > maxFreq:
                count = 1
                maxFreq = myDict[i]
                continue
            
            if myDict[i] == maxFreq:
                count += 1

        return count*maxFreq
