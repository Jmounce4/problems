# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            myGuess = 2
        else:
            myGuess = n/2

        increment = max(myGuess/2, 1)

        result = guess(myGuess)

        while result != 0:
            

            if result == 1:
                myGuess+=increment


            if result == -1:
                myGuess-=increment


            result = guess(myGuess)
            
            increment = max(increment / 2, 1)

        return myGuess
