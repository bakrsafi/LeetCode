# this is my way not efficient but it works
# it cuse two loops to check for the longest substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        for c in range(len(s)):
            arr = [] 
            for x in range(c, len(s)):
                if s[x] in arr:
                    if len(arr) > max_length:
                        max_length = len(arr)
                    break 
                arr.append(s[x])
            if len(arr) > max_length:
                max_length = len(arr)
        return max_length 

# the way i learned 
# it is using a sliding window technisue with two pointers to keep track of the current substring without repeating characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        left = 0 
        max_length = 0   
        for right in range(len(s)):  
            while s[right] in chars:
                chars.remove(s[left])
                left += 1  
            chars.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

