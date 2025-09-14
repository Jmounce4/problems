class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        vowels = set('aeiou')
        returnArray = []
        
        
        def mask_vowels(word):
            masked = ''
            for c in word.lower():
                if c in vowels:
                    masked += '*'
                else:
                    masked += c
            return masked
        

        exactSet = set(wordlist)
        lowerDict = {}
        vowelDict = {}
        
        for word in wordlist:
            word_lower = word.lower()
            word_vowel = mask_vowels(word)
            
            if word_lower not in lowerDict:
                lowerDict[word_lower] = word
            if word_vowel not in vowelDict:
                vowelDict[word_vowel] = word
        

    

        for query in queries:
            query_lower = query.lower()
            query_vowel = mask_vowels(query)
            
            if query in exactSet:
                returnArray.append(query)
            
            elif query_lower in lowerDict:
                returnArray.append(lowerDict[query_lower])
            
            elif query_vowel in vowelDict:
                returnArray.append(vowelDict[query_vowel])
            
            else:
                returnArray.append('')
        
        return returnArray



#Below is my original approach that exceeded time limit


  
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        returnArray = []
        vowels = set("aeiouAEIOU")
        vowelWordList = ''

        for i in range(len(queries)):
            temp = ""
            caseMatch = None
            vowelMatch = None
            query_lower = queries[i].lower()
            query_vowel = ''.join('*' if ch in vowels else ch for ch in query_lower)

            for j in range(len(wordlist)):
                word_lower = wordlist[j].lower()
                word_vowel = ''.join('*' if ch in vowels else ch for ch in word_lower)

                if wordlist[j] == queries[i]:
                    returnArray.append(wordlist[j])
                    break
                elif caseMatch is None and word_lower == query_lower:
                    caseMatch = wordlist[j]
                elif vowelMatch is None and word_vowel == query_vowel:
                    vowelMatch = wordlist[j]

                if j == len(wordlist) - 1:
                    if caseMatch:
                        returnArray.append(caseMatch)
                    elif vowelMatch:
                        returnArray.append(vowelMatch)
                    else:
                        returnArray.append(temp)
                    

        return returnArray




    
