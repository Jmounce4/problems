class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        sortedList = nums.sort()
        newArray = []
        for i in range(0, len(nums), 3):
            first = nums[i]
            second = nums[i+1]
            third = nums[i+2]
            if nums[i+2] - nums[i] <= k:
                newArray.append([first, second, third])
            else:
                return []
            

        return newArray
