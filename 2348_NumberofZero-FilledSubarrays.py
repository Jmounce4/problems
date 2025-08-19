class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0
        
        current = 0

        for i in range(len(nums)):
            
            if nums[i] == 0:
                current+=1
            if  i+1 < len(nums) and nums[i+1] == 0:
                continue
            
            for j in range(current+1):
                total += j
            
            current = 0

        return total
