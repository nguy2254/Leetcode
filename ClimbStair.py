class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(n):
            if n == 0:
                fac = 1
            if n != 0:
                fac = 1
                for i in range(1,n+1):
                    fac = fac*i
            return fac
        onestep = []
        twostep = [] 
        combinations = [] 
        for i in range(n//2+1):
            twostep.append(i)
            onestep.append(n-i*2)
        for num1, num2 in zip(onestep,twostep):
            x = factorial(num1+num2)/ (factorial(num1)* factorial(num2))
            combinations.append(x)
        return sum(combinations)

   #An elegant Fibonaci way: 
   def climbStairs1(self, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n-1)+self.climbStairs(n-2)
 
