class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        counter = 0
        total = 0
        for i in range(len(timeSeries)):
            counter = duration
            if i < len(timeSeries)-1:
                diff = (timeSeries[i+1] - timeSeries[i])
                if diff >= duration:
                    total += counter
                else:
                    total += diff
                counter = 0
        total += counter
        return (total)
