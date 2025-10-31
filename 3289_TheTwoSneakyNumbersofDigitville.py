class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

        mySet = set()
        tracking = []

        for i in nums:
            if i in mySet:
                tracking.append(i)
            else:
                mySet.add(i)
        
        return tracking
