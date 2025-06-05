class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'n': 'n',
        'o': 'o',
        'p': 'p',
        'q': 'q',
        'r': 'r',
        's': 's',
        't': 't',
        'u': 'u',
        'v': 'v',
        'w': 'w',
        'x': 'x',
        'y': 'y',
        'z': 'z'
    }
        def find(x):
            if parent[x] == x: 
                return x
            root = find(parent[x])
            return root

        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA < rootB:
                parent[rootB] = rootA
            else: 
                parent[rootA] = rootB


        myString = ''

        for i in range(len(s1)):
            union(s1[i], s2[i])
        for c in baseStr:
            myString += find(c)
        return myString
