class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        flatArray = []
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                flatArray.append(grid[r][c])
                

        flatArray = sorted(flatArray)
        medianIndex = int((len(flatArray)/2))
        median = flatArray[medianIndex]
        count = 0
        for i in flatArray:
            diff = abs(i - median)
            if diff % x != 0:
                return -1
            count += (diff//x)

        return count                                                                                 
