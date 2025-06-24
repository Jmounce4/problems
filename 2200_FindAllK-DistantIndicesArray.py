class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """

        indexSet = set()

        for i in range(len(nums)):
            if nums[i] == key:
                before = max(0, i - k)
                after = min(i + k, len(nums)-1)+1
                for j in range(before, after):
                    indexSet.add(j)
        return sorted(indexSet)
