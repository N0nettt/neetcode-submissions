class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        if n > 0:
            for i in range(n):
                res *= x
        elif n < 0:
            n = n * (-1)
            for i in range(n):
                res *= x
                print(res)
            res = 1/res
        else:
            res = 1

        return res
