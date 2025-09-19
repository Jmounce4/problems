class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        
        self.spreadsheetDict = {}
        uppercase_letters = list(string.ascii_uppercase)
        for j in uppercase_letters:
            for i in range(1, rows+1):
                self.spreadsheetDict[str(j)+(str(i))] = 0
        #print(self.spreadsheetDict)
        
        

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.spreadsheetDict[cell] = value
        

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        self.spreadsheetDict[cell] = 0
        

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        buildString = ''
        first = ''
        second = ''
        checkNext = 0
        for i in formula:
            if i == '=':
                continue
            if i == '+':
                first = buildString
                buildString = ''
                continue
            buildString += i
        
        second = buildString
        
        if first.isdigit():
            value1 = first
        else: 
            value1 = self.spreadsheetDict[first]


        if second.isdigit():
            value2 = second
        else:       
            value2 = self.spreadsheetDict[second]

        return int(value1) + int(value2)



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
