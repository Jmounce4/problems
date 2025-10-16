class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        total = 0
        counter = 0
        

        if len(s) == 0 or len(g) == 0:
            return total

        for i in g:
            check = 0
            while check == 0:
                if counter <= len(s)-1:
                    if s[counter] >= i:
                        total+=1
                        check = 1
                    counter+=1
                else:
                    break
            #counter+=1

        return total
