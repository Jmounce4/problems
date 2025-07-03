class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        
        word = ['a']
        while len(word) < k:
            next_chars = []
            for ch in word:
                next_ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
                next_chars.append(next_ch)
            word.extend(next_chars)
        return word[k - 1]
