class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        minimumDiff = max(nums)

        if k == 1 or len(nums) == 1:
            return 0

        for i in range(len(nums)-k+1):
            subSet = []
            for j in range(k):
                subSet.append(nums[i+j])
            
            minSub = min(subSet)
            maxSub = max(subSet)
            currentSum = maxSub - minSub

            

            if currentSum < minimumDiff:
                minimumDiff = currentSum

        return minimumDiff 
            
