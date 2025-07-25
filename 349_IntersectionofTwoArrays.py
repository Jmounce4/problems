class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        set1 = set()
        set2 = set()
        newArray = []

        for i in nums1:
            if i not in set1:
                set1.add(i)
                

        for j in nums2:
            if j in set2:
                continue
            if j in set1:
                newArray.append(j)
                set2.add(j)
        
        return newArray
                
                #can just set(nums1) and set(nums2)
                #return list(set(nums1) and set(nums2) is a quick solution
