class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        isCyclical = False

        while True:

            if n in seen:
                break

            seen.add(n)
            newN = 0
            while n != 0:
                digit = n % 10
                newN += math.pow(digit, 2)
                n = n // 10

            if newN == 1:
                isCyclical = True
                break
            
            n = newN
            
        return isCyclical