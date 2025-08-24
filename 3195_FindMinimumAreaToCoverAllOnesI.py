class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        left = None
        right = None
        up = None
        down = None

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == 1:
                    if left is None or left > i:
                        left = i
                    if right is None or right < i:
                        right = i
                    if up is None or up > j:
                        up = j
                    if down is None or down < j:
                        down = j


        area = (1+right - left) * (1+down - up)
        return area
