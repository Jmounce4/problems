class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                magazine = magazine.replace(letter, '', 1)
        
        return True
