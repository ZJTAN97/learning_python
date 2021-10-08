class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        currMax = nums[0]

        for num in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += num
            currMax = max(currMax, currSum)
        
        return currMax


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))