class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []

        def backtrack(start):

            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):

                if isPalindrome(s, start, end):
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()   # backtrack

        def isPalindrome(s, l, r):
            substring = s[l:r+1]
            return substring == substring[::-1]

        backtrack(0)
        return res
