class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        isValid = True


        #Checking rows
        for row in board:
            usedVal = set()
            for val in row:
                if val == '.':
                    continue
                if val in usedVal:
                    isValid = False
                    return isValid
                else:
                    usedVal.add(val)

        #Checking columns
        for column in range(9):
            usedVal = set()
            for row in range(9):
                if board[row][column] == '.':
                    continue
                if board[row][column] in usedVal:
                    isValid = False
                    return isValid
                else:
                    usedVal.add(board[row][column])

        
        #Checking 3x3's

        for boxRow in [0, 3, 6]:
            for boxColumn in [0, 3, 6]:
                usedVal = set()
                for i in range(3):
                    for j in range(3):
                        if board[boxRow+i][boxColumn+j] == '.':
                            continue
                        if board[boxRow+i][boxColumn+j] in usedVal:
                            isValid = False
                            return isValid
                        else:
                            usedVal.add(board[boxRow+i][boxColumn+j])



        return isValid
