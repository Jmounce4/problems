class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digit_list = list(map(int, str(num)))
        numString = ''
        changed = False
        for nums in digit_list:
            if changed == False:
                if nums == 6:
                    nums = 9
                    changed = True
            numString += str(nums)
        
        return int(numString)
