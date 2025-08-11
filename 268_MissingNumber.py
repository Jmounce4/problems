class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)

        previous = -1
        for i in sort:
            if i == previous+1:
                previous = i
            else:
                return previous+1
            
            if i == sort[-1]:
                return i+1
