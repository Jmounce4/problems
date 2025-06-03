class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftPointer = 0
        rightPointer = len(height)-1
        maxArea = 0
        
        while leftPointer < rightPointer:
            #multiply the lower height of the 2, and the distance between the 2 indexes. Update when new Max
            newArea = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
            if newArea > maxArea:
                maxArea = newArea
            
            #move pointer left right if shorter & vice versa
            if height[leftPointer] < height[rightPointer]:
                leftPointer+=1
            else:
                rightPointer-=1

        return maxArea
