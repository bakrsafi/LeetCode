# 150. Evaluate Reverse Polish Notation


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """ 
        
        
        s = []
        for x in tokens:

            if x.lstrip("-").isdigit():
                s.append(int(x))
            elif x == '*':
                res = s.pop()*s.pop()
                s.append(res)
            elif x == '+':
                res = s.pop()+s.pop()
                s.append(res)
            elif x == '-':
                res = -s.pop()+s.pop()
                s.append(res)
            elif x == '/':
                a = s.pop()
                b = s.pop()
                s.append(int(b / a) if b * a >= 0 else -(-b // a))
        
        print(res)
        return res

                

        
        
tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
sol.evalRPN(tokens)