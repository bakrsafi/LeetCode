# 53. Maximum Subarray
# the objective is to find the contiguous subarray within an array (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        currentSum = 0
        maxSum = nums[0]

        for num in nums:
            currentSum += num
            maxSum = max(maxSum, currentSum)

            if currentSum < 0:
                currentSum = 0

        return maxSum
    