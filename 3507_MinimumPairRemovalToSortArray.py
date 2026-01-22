class Solution(object):
    def minimumPairRemoval(self, nums):
        totalOperations = 0

        def isNonDecreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        while not isNonDecreasing(nums):


            minIndex = 0
            minSum = nums[0] + nums[1]

 
            for i in range(1, len(nums) - 1):
                pairSum = nums[i] + nums[i + 1]
                if pairSum < minSum:
                    minSum = pairSum
                    minIndex = i

            nums[minIndex] = nums[minIndex] + nums[minIndex + 1]
            nums.pop(minIndex + 1)

            totalOperations += 1

        return totalOperations


""" unintended code from overcomplicating the problem due to instructions unclear


        descending = False
        totalOperations = 0

        while descending is False:
            
            operations = 0
            newNums = []
            i = 0
            while i < len(nums)-1:
                if nums[i] > nums[i+1]:
                    
                    if i > 0:
                        if nums[i+1] >= nums[i-1]:
                            newNums.append(nums[i] + nums[i-1])
                            
                            operations+=1
                        else:
                            newNums.append(nums[i] + nums[i+1])
                            
                            operations+=1
                    else:
                        newNums.append(nums[i] + nums[i+1])

                        operations+=1
                    
                    i+=2
                else:
                    newNums.append(nums[i])
                    i+=1
            
            totalOperations += operations
            

            if operations == 0:
                descending = True
            
            nums = newNums

        return totalOperations
            """

