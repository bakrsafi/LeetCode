# 152. Maximum Product Subarray
# the objective is to find the contiguous subarray within an array (containing at least one number) which has the largest product and return its product.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 1
        curr = nums[0]
        for x in range(len(nums)):
            for y in range(x,len(nums)):
                max = max * nums[y]
                if max >= curr:
                    curr = max
            max = 1
        print(curr)
        return curr
        
        
        
   