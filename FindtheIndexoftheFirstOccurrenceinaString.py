# 28. Find the Index of the First Occurrence in a String
# the objective is to find the index of the first occurrence of the substring "needle" in the string "haystack". If "needle" is not found in "haystack", return -1.
# my way of solving this problem 
class Solution(object):
    def strStr(self, haystack, needle):

        if needle in haystack :
            return haystack.find(needle)
        else:
            return -1

# the way i learned from chatgpt 
class Solution(object):
    def strStr(self, haystack, needle):

        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
            


