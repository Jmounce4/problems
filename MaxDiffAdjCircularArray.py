class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDiff = abs(nums[-1] - nums[0])
        
        for i in range(len(nums)-1):
            if i != len(nums):
                currentDiff = abs(nums[i] - nums[i+1])
            if  currentDiff > maxDiff:
                maxDiff = currentDiff
            
            i + 1

        return maxDiff
