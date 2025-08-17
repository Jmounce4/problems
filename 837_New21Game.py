class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >=  k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n+1)
        dp[0] = 1.0

        window_sum = 1.0
        result = 0.0

        for x in range(1, n+1):
            dp[x] = window_sum/maxPts

            if x < k:
                window_sum+=dp[x]
            else:
                result+=dp[x]

            if x - maxPts >= 0:
                window_sum -= dp[x-maxPts]
        
        return result
