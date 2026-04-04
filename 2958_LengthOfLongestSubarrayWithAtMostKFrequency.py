class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        longest = 0
        left = 0
        subDict = {}
        for i in range(len(nums)):
            if nums[i] not in subDict:
                subDict[nums[i]] = 1
            else:
                subDict[nums[i]] += 1
            
            while subDict[nums[i]] > k:
                subDict[nums[left]] -= 1
                left += 1


            longest = max(longest, i - left + 1)
        
        return longest

        
        ''' O(n^2)
        longest = 0
        if len(nums) == 1:
            return 1
        for i in range(len(nums)):
            subDict = {}
            tempLength = 0
            for j in range(i, len(nums)):
                if nums[j] not in subDict:
                    subDict[nums[j]] = 1
                    tempLength+=1
                else:
                    if subDict[nums[j]] < k:
                        subDict[nums[j]] += 1
                        tempLength+=1
                    else:
                        break
                if tempLength > longest:
                    longest = tempLength
                    
        
        return longest
        '''
