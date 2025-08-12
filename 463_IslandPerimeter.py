class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] is 1:
                    perimeter+=4
                else:
                    continue
                if j > 0 and grid[i][j-1] is 1:
                    perimeter-=1
                if j < len(grid[i])-1 and grid[i][j+1] is 1:
                    perimeter-=1
                if i > 0 and grid[i-1][j] is 1:
                    perimeter-=1
                if i < len(grid)-1 and grid[i+1][j] is 1:
                    perimeter-=1

        return perimeter
