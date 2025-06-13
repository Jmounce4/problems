class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()



        low = 0
        #Highest and lowest after sort
        high = nums[-1] - nums[0]
        

        while low < high:
            mid = (low + high)//2

            
            countedPairs = 0
            i = 0
            
            
            while i < len(nums)-1:
                if abs(nums[i] - nums[i+1]) <= mid:
                    countedPairs+=1
                    i+=2
                else:
                    i+=1

            if countedPairs >= p:
                high = mid
            else:
                low = mid + 1

        return low
