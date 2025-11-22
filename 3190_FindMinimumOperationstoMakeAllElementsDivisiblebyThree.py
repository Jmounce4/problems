class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0

        for i in nums:
            if (i % 3) != 0:
                counter+=1

        return counter
