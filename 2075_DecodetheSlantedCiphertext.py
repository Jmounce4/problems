class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        
        if rows == 1:
            return encodedText

        columns = int(len(encodedText) /  rows)
        #print(columns)

        matrix = [[0] * columns for _ in range(rows)]

        tempColumn = 0
        tempRow = 0

        for i in range(len(encodedText)):
            if tempColumn < columns and tempRow < rows:
                matrix[tempRow][tempColumn] = encodedText[i]
                tempColumn += 1
            if tempColumn >= columns:
                tempColumn = 0
                tempRow += 1
        
        #print(matrix)
        result = []

        
        for startCol in range(columns):
           r = 0
           c = startCol
           while r < rows and c < columns:
                result.append(matrix[r][c])
                r += 1
                c += 1
        
        #print(stringBuild)

        return ''.join(result).rstrip()
