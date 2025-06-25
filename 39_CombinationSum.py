class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        myList = []
        candidates.sort()
        
        def helperFunction(currentList, nextIndex, currentSum):
            
            if currentSum == target:
                myList.append(list(currentList))
                return
            if currentSum > target:
                return
            if currentSum < target:
                for i in range(nextIndex, len(candidates)):
                    currentList.append(candidates[i])
                    helperFunction(currentList, i, currentSum + candidates[i])
                    currentList.pop()

        helperFunction([], 0, 0)

        return myList
