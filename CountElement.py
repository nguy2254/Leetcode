class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dict = {} 
        for i in arr:
            dict[i] = dict.get(i, 0) + 1
        count = 0 
        for i in dict:
            if dict.get(i+1) != None : count = count + dict[i] 
        return count 
