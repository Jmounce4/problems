class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        scores = []
        counter = 0
        for i in range(len(operations)):
            
            if operations[i] == '+':
                if counter > 1:
                    scores.append(scores[counter-1] + scores[counter-2])
            elif operations[i] == 'D':
                if counter > 0:
                    scores.append(scores[counter-1]*2)
            elif operations[i] == 'C':
                if counter > 0:
                    scores.pop()
                    counter -= 1
                    continue
            else:
                scores.append(int(operations[i]))

            counter+=1

        return sum(scores)
            
