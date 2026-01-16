class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        RCount = 0
        LCount = 0
        UCount = 0
        DCount = 0

        for i in moves:
            if i == 'R':
                RCount += 1
            if i == 'L':
                LCount += 1
            if i == 'U':
                UCount += 1
            if i == 'D':
                DCount += 1

        if RCount == LCount and UCount == DCount:
            return True
        else:
            return False
        
