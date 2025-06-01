class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        myList = []

        #if left '(' then a right ')' can be put
        def helpFunction(current, left, right):
            if left == n and right == n:
                myList.append(current)
            if left <= n:
                helpFunction(current + "(", left+1, right)
            if right < left:
                helpFunction(current + ")", left, right+1)
            
        helpFunction("", 0, 0)
        return myList
