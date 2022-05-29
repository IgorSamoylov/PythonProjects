

class Solution:
    
    def reverse(self, x: int) -> int: 
        sign = "-" if x < 0 else ""
        result = int(sign + str(abs(x))[::-1])
        
        if -2147483648 < result < 2147483647:
            return result
        return 0


solution = Solution()
print(solution.reverse(-123))
