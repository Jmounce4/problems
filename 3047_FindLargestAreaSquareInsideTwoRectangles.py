class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        
        
        maxArea = 0
        for i in range(len(bottomLeft)):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i+1, len(bottomLeft)):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                ix1 = max(x1, x3)
                iy1 = max(y1, y3)
                ix2 = min(x2, x4)
                iy2 = min(y2, y4)

                if ix1 < ix2 and iy1 < iy2:
                    width = ix2 - ix1
                    height = iy2 - iy1

                    side = min(width, height)
                    maxArea = max(maxArea, side * side)


        return maxArea
            
