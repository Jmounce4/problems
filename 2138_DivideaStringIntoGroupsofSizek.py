class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        myList = []
        groups = (len(s) + k - 1) // k
        partition = ""
        for i in range(0, len(s), k):
            if (i+k) > len(s):
                fillAmount = (i+k)-len(s)
                partition = s[i:]
                for j in range(fillAmount):
                    partition += fill
            else:
                partition = s[i:i+k]
            
            myList.append(partition)

        return myList
