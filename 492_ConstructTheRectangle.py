class Solution(object):
    import math
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        root = math.sqrt(area)
        width = int(math.floor(root))
        length = int(math.ceil(root))
        while length*width != area:
            if length*width > area:
                width-=1
            
            if length*width < area:
                length+=1

        
        result = [length, width]
        return result
