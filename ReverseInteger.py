# My solution
class Solution(object):
    def reverse(self, x):
        if (x>=0) :
            string_old = str(int(x))
            string_new = ""
            for i in range(len(string_old)):
                print(i)
                j = len(string_old) - i 
                string_new += string_old[j-1]
            result = int(string_new)
            if ((result < -2**31) or (result> 2**31-1)):
                  result = 0
            return result
        else:
            string_old = str(abs(x))
            string_new = ""
            for i in range(len(string_old)):
                j = len(string_old)  - i 
                string_new += string_old[j-1]
            result = -int(string_new)            
            if ((result < -2**31) or (result> 2**31-1)):
                  result = 0
            return result
 #Real solution            
class Solution(object):
    def reverse(self, x):        
        if (x>=0) :
            result = int(str(int(x))[::-1])
            if ((result < -2**31) or (result> 2**31-1)):
                  result = 0
            return result
        else:
            result = -int(str(abs(x))[::-1])
            if ((result < -2**31) or (result> 2**31-1)):
                  result = 0
            return result
                  result = 0
            return result
