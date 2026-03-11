# 29. Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod
# this is my way to solve the problem, but it is not efficient enough, so I will try to optimize it by using bit manipulation
# not the best solution, but it is a good way to understand the problem and the solution
class Solution(object):
    def divide(self, dividend, divisor):
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        counter = 0
        
        while dividend >= divisor:
            temp = 1
            
            while dividend >= (temp * 2) * divisor:
                temp *= 2
            
            dividend -= temp * divisor
            counter += temp
        
        result = counter * sign
        
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
            
        return result

# this is the optimized solution, it uses bit manipulation to speed up the process of finding the suotient
# it works by shifting the divisor to the left until it is greater than the dividend, and then subtracting the shifted divisor from the dividend and adding the corresponding power of 2 to the result
# more faster than the previous solution, but it is still not the best solution, as it still has a time complexity of O(log n)
class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result += 1 << i
                dividend -= divisor << i
        
        return result * sign