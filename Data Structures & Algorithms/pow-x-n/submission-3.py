class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            half = power(x, n//2)

            if n % 2 == 0:
                return half*half
            else:
                return half*half*x
        
        res = 1
        if n < 0:
            res = power(x, -n)
            res = 1/res
        else:
            res = power(x, n)
        
        return res


            
