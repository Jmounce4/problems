class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        harmDict = {}
        
        for i in range(len(nums)):
            if nums[i] in harmDict:
                harmDict[nums[i]] += 1
            else:
                harmDict[nums[i]] = 1

        finalLength = 0
        harmLength = 0
        for key in harmDict:
            if key+1 in harmDict:
                harmLength = harmDict[key] + harmDict[key+1]
            if harmLength > finalLength:
                finalLength = harmLength

        return finalLength
