class Solution(object):
    def isHappy(self, n):
        visited = set()
        while 1:
            if n == 1:
                return True 
                break 
            sum_digit = sum(int(digit)**2 for digit in str(n))
            if sum_digit in visited:
                return False
                break
            visited.add(sum_digit)
            n = sum_digit
