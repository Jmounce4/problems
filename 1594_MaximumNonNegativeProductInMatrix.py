class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        calcGrid = [[(0, 0) for _ in range(cols)] for _ in range(rows)]

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #left = (None, None)
                #top = (None, None)
                if r == 0 and c == 0:
                    calcGrid[r][c] = (grid[r][c], grid[r][c])
                    continue
                
                if c > 0:
                    left = calcGrid[r][c-1]
                else:
                    left = None

                if r > 0:
                    top = calcGrid[r-1][c]
                else:
                    top = None
            
                candidates = []

                if left:
                    candidates.extend([left[0] * grid[r][c], left[1] * grid[r][c]])
                if top:
                    candidates.extend([top[0] * grid[r][c], top[1] * grid[r][c]])
                
                calcGrid[r][c] = (min(candidates), max(candidates))
        
        print calcGrid
        answer = max(calcGrid[rows-1][cols-1])
        
        MOD = 10**9 + 7

        if answer >= 0:
            return answer%MOD
        else:
            return -1
                
