class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        current = ''
        prev = ''

        for i in s:
            if i == ' ':
                if current != '':
                    prev = current
                current = ''
            else:
                current += i
            
            
        if current != '':
            return len(current)
        else:
            return len(prev)
