class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        myDict1 = {}
        myDict2 = {}

        for i in s:
            if i not in myDict1:
                myDict1[i] = 1
            else:
                myDict1[i] +=1

        for i in t:
            if i not in myDict2:
                myDict2[i] = 1
            else:
                myDict2[i] +=1

        if myDict1 == myDict2:
            return True
        else:
            return False
