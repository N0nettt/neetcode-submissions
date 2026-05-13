class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit = int(num1[i]) * int(num2[j])

                
                res[i+j+1] += digit
                res[i+j] += res[i+j+1] // 10
                res[i+j+1] = res[i+j+1] % 10

        # remove leading zeros
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        return "".join(map(str, res[beg:]))