class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        sumList = []
        while sum != 1 :
            sum = 0
            while n > 0:
                digit = n%10
                sum += digit*digit
                n = n // 10
            if (sum in sumList):
                return False
            sumList.append(sum)
            n = sum 
        if (sum == 1):
            return True
        return False
