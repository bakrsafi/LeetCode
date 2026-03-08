# 34. Find First and Last Position of Element in Sorted Array
# the objective is to find the first and last position of a given target in a sorted array. If the target is not found, return [-1, -1]. The solution iterates through the array from both ends simultaneously, checking for the target and updating the positions accordingly. The time complexity is O(n) in the worst case, but it can be optimized to O(log n) using binary search since the array is sorted.
# thsi is the first solution which is not optimized and the second one is optimized using break statement to stop the loop once both positions are found.
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = -1
        y = -1
        temp1 = 0
        temp2 = 0
        arr=[]
        for i in range(len(nums)):
            j=len(nums)-1-i
            if nums[i] == target and temp1 == 0:
                x=i
                temp1 = 1
            if nums[j] == target and temp2 == 0:
                y=j
                temp2 = 1

        if x == -1 and y>-1:
            arr.append(y)
            arr.append(y)
        elif y == -1 and x>-1:
            arr.append(x)
            arr.append(x)
        else :
            arr.append(x)
            arr.append(y)
        return arr    
        
# optimized solution using break statement to stop the loop once both positions are found.
# This solution iterates through the array from both ends simultaneously, checking for the target and updating the positions accordingly. The time complexity is O(n) in the worst case, but it can be optimized to O(log n) using binary search since the array is sorted.
class Solution(object):
    def searchRange(self, nums, target):
        x, y = -1, -1
        n = len(nums)

        for i in range(n):
            j = n - 1 - i

            if x == -1 and nums[i] == target:
                x = i

            if y == -1 and nums[j] == target:
                y = j

            if x != -1 and y != -1:
                break

        return [x, y]


