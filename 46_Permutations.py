class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permList = []
        def helpFunction(current, remaining):
            if not remaining:
                permList.append(current)
                return
            for number in remaining:
                nextVal = current + [number]
                index = remaining.index(number)
                nextRemaining = remaining[:index] + remaining[index+1:]
                helpFunction(nextVal, nextRemaining)


        helpFunction([], nums)
        return permList
