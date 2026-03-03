# 1929. Concatenation of Array
# the objective is to concatenate the array with itself, so we can simply add the array to itself or we can create a new array and fill it with the values of the original array twice.
# this is my way of solving the problem
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums +=nums
        return nums

# this is tha fastest way using list comprehension to solve the problem with python 
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        arr = [0] * (2 * l)
        for i in range(l):
            arr[i]=nums[i]
            arr[i+l]=nums[i]
        return arr 
        
