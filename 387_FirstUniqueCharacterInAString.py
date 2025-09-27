class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        uniqueSet = set()
        removedSet = set()
        for i in range(len(s)):
            if s[i] in uniqueSet:
                uniqueSet.remove(s[i])
                removedSet.add(s[i])
            elif s[i] in removedSet:
                continue
            else:
                uniqueSet.add(s[i])

        if uniqueSet:
            for i in range(len(s)):
                if s[i] in uniqueSet:
                    return i
        else:
            return -1

        """ double loop approach
        counter = 0
        unique = -1
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    counter+=1
                if counter > 1:
                    break
                if j == len(s)-1:
                    unique = i
            if counter <= 1:
                break
            counter = 0

        return unique
        """
