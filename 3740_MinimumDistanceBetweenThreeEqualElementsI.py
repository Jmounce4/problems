class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        removedSet = set()
        minDistance = 1000

        for i in range(len(nums)):
            if nums[i] not in removedSet:
                equal = []
                if i < len(nums)-1:
                    for j in range(i+1, len(nums)):
                        if nums[j] == nums[i]:
                            equal.append(j)
                        if len(equal) == 2:
                            distance = abs(i - equal[0]) + abs(equal[0] - equal[1]) + abs(equal[1] - i)
                            minDistance = min(minDistance, distance)
                if len(equal) < 2:
                    removedSet.add(nums[i])

        if minDistance < 1000:
            return minDistance
        else:
            return -1
