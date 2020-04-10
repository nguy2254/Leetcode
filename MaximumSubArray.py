class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentsum , maxsum = nums[0], nums[0]
        for num in nums[1:]:
            currentsum = max(num,currentsum+num)
            maxsum = max(currentsum, maxsum)
        return maxsum
        
