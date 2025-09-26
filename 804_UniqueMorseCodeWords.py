class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse_map = {
            'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..",
            'e': ".",  'f': "..-.", 'g': "--.",  'h': "....",
            'i': "..", 'j': ".---", 'k': "-.-",  'l': ".-..",
            'm': "--", 'n': "-.",   'o': "---",  'p': ".--.",
            'q': "--.-",'r': ".-.", 's': "...",  't': "-",
            'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
            'y': "-.--", 'z': "--.."
            }

        if len(words) == 1:
            return 1

        tracker = set()
        nextVal = ''
        counter = 0
        for i in words:
            for j in i:
                nextVal += morse_map[j]
            if nextVal not in tracker:
                counter+=1
                tracker.add(nextVal)
            nextVal = ''


        return counter
