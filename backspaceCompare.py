class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def getstring(string):
            result =[]
            strip = 0 
            for i in string[::-1]:
                if i == '#':
                    strip+=1
                elif strip>0:
                    strip-=1
                else:
                    result.append(i)
            return result
                
        return getstring(S) == getstring(T)
    
        def getstring(string):
            result = []
            for i in string:
                if i != '#':
                    result.append(i)
                if i == '#' and result != []:
                    result.pop()
            return result
        return getstring(S) == getstring(T)
