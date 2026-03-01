# problem link: https://leetcode.com/problems/two-sum/


# my way useing for loops it cause n(O)
class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# chat gpt way
# i have learned that using hash map is more efficient than using for loops because it allows us to store and retrieve values in constant time, which can significantly reduce the time complexity of the algorithm.
# using hash map it cause n(O) and space O(n)         
class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in lookup:
                return [lookup[complement], i]
            
            lookup[num] = i