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
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        point1= 0
        point2= 1 
        arr.sort()
        count = 0
        
        for i in arr[:len(arr)-1]: 
            if arr[point1] == arr[point2] - 1: 
                count = count + point2 - point1
                point1 = point2
                point2 = point2 +1 
            elif arr[point1] == arr[point2] : 
                point2 = point2 +1 
            else:
                point1 = point2
                point2 = point2 +1 
        return count 
