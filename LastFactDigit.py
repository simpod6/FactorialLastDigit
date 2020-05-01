import math

class LastFactDigit:

    def leaveLastNonZeroDigit(x, digits):
        while x % 10 == 0:
            x = x / 10        
        return x % (10 ** digits)

    def calcLastFactDigit(num):
        n = 1
        for i in range(1, num + 1):            
            n = i * n
            n = LastFactDigit.leaveLastNonZeroDigit(n, len(str(i))+2)
            
        n = LastFactDigit.leaveLastNonZeroDigit(n, 1)
        return int(n)

