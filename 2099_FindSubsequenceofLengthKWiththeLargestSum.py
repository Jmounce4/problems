class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        indexed = []
        for i in range(len(nums)):
            val = nums[i]
            indexed.append((val, i))
        indexed.sort(reverse = True)
        subK = indexed[:k]
        result = sorted(subK, key=lambda x: x[1])
        return [val for val, i in result]
