class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        currentMin = nums[0]
        currentMax = 0
        count = 1
       
        for i in range(len(nums)):
            if nums[i] >= currentMax:
                currentMax = nums[i]
            if (currentMax - currentMin) > k:
                count+=1
                currentMin = nums[i]
        return count
