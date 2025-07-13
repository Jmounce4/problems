class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDict = {}

        for i in range(len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]] += 1
        
        for i in numsDict:
            if numsDict[i] != 2:
                return i
