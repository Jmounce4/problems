class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        current = 0
        previous = 0
        for char in s[::-1]:
            value = roman_map[char]
            if value < previous:
                value = (roman_map[char])*-1
            previous = value
            current += value
        return current
