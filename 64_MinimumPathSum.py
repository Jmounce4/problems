class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        memoryDict = {}
        m = len(grid)
        n = len(grid[0])

        def helper(v, h):


            #This path cost is already calculated
            if (v, h) in memoryDict:
                return memoryDict[(v, h)]
            #Reaches end, return final space cost
            if v == m-1 and h == n-1:
                return grid[v][h]
            
            minimum = 100000

            #If can go this direction, find path with minimum cost
            if v < m-1:
                minimum = min(minimum, helper(v+1, h))

            if h < n-1:
                minimum = min(minimum, helper(v, h+1))

            #Stores Coordinate with minimum path
            memoryDict[(v,h)] = grid[v][h] + minimum

            return memoryDict[(v,h)]

        return helper(0,0)
            
