class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """


        orderedList = []
        

        def DFSLexical(root, next):
            orderedList.append(next)
            if (next * 10) <= n:
                DFSLexical(root, next*10)
            if next+1 <= root and next % 10 != 9:
                DFSLexical(root, next+1)
        
        DFSLexical(n, 1)

        return orderedList
