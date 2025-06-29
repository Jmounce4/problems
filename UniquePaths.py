class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        memoryDict = {}

        def helper(v, h):
            #everytime a path reaches, +1
            if v == m-1 and h == n-1:
                return 1

            if (v, h) in memoryDict:
                return memoryDict[(v, h)]


            if v < m-1:
                goDown = helper(v+1, h)
            else: 
                goDown = 0
            if h < n-1:
                goRight = helper(v, h+1)
            else:
                goRight = 0
            
            memoryDict[(v, h)] = goDown + goRight
            return memoryDict[(v, h)]

        return helper(0, 0)
