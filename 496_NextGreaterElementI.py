class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nextGreaterArr = []

        for i in nums1:
            nextGreater = -1
            selected = False
            for j in nums2:
                if j == i:
                    selected = True
                if not selected:
                    continue
                if j > i:
                    nextGreater = j
                    break

            nextGreaterArr.append(nextGreater)

        return nextGreaterArr
