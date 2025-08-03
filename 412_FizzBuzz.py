class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        myArray = []
        
        for i in range(1,n+1):
            tempString = ''
            if i % 3 == 0:
                tempString += 'Fizz'
            if i % 5 == 0:
                tempString += 'Buzz'
            
            if tempString == '':
                myArray.append(str(i))
            else:
                myArray.append(tempString)

        return myArray
