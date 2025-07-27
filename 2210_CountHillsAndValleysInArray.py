class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        counter = 0
        for i in range(len(nums)):
            
            check1 = 0
            if i == 0:
                continue
            if i == len(nums)-1:
                break
            
            if nums[i] > nums[i-1]:
                check1 = 1
            if nums[i] < nums[i-1]:
                check1 = -1


            while nums[i] == nums[i+1] and i+1 < len(nums)-1:
                i+=1
            
            if nums[i] > nums[i+1] and check1 == 1:
                counter+=1
            if nums[i] < nums[i+1] and check1 == -1:
                counter+=1
        
        return counter
