class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        number = 0
        
        for i in range(n):
            number += digits[i] * (10**(n-i-1))
        
        number += 1
        newDigits = []

        while number != 0:
            digit = number % 10
            number = number // 10
            newDigits.append(digit)

        d = []
        for i in range(len(newDigits)-1, -1, -1):
            d.append(newDigits[i])

        return d
    
        