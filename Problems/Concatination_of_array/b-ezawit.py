class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        length = len(nums)
        for i in range(2 * length):
            if i < length:
                ans.append(nums[i])
            else:
                ans.append(nums[i-length])
        
        return ans
            
