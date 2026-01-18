class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxPerimeter = min(len(grid), len(grid[0]))
        currentMax = 1

        for i in range(len(grid)):
            
            for j in range(len(grid[i])):

                #check squares based on current max square + 1, since we look for bigger square
                for k in range(currentMax+1, maxPerimeter+1):
                
                    #dimension check to not go out of bounds
                    if i + k > len(grid) or j + k > len(grid[0]):
                        continue
                    
                    target = None
                    valid = True

                    for r in range(k):
                        rowSum = 0
                        for c in range(k):
                            rowSum += grid[i+r][j+c]

                        if target is None:
                            target = rowSum
                        elif rowSum != target:
                            valid = False
                            break

                    for c in range(k):
                        colSum = 0
                        for r in range(k):
                            colSum += grid[i+r][j+c]

                        if colSum != target:
                            valid = False
                            break

                    diag1 = diag2 = 0
                    for t in range(k):
                        diag1 += grid[i+t][j+t]
                        diag2 += grid[i+t][j+k-1-t]

                    if diag1 != target or diag2 != target:
                        valid = False
                    
                    if valid:
                        currentMax = max(currentMax, k)

        return currentMax
