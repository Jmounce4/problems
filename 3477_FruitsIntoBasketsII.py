class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        unplaced = len(fruits)

        usedBaskets = set()

        for i in range(len(fruits)):

            for j in range(len(baskets)):

                if fruits[i] <= baskets[j] and j not in usedBaskets:
                    usedBaskets.add(j)
                    unplaced -= 1
                    break
        

        return unplaced
