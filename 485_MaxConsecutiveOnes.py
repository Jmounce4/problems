class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        current = 0
        for i in nums:
            if i == 1:
                current+=1
                if current > counter:
                    counter = current
            else:
                current = 0

        return counter
