class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        disappeared = []
        rangeSet = list(set(range(1,len(nums)+1)))
        numsSet = set(nums)

        for i in rangeSet:
            if i not in numsSet:
                disappeared.append(i)

        return disappeared
