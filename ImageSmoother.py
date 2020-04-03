class Solution(object):
    def imageSmoother(self, x):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        from copy import deepcopy
        num_row = len(x)
        num_column = len(x[0])
        y  = deepcopy(x)
        def get_value(x,i,j):
            if (i <0) or (j<0):
                return None
            try:
                return x[i][j]
            except IndexError:
                return None
        def sum_nonzero(x):
            summary = 0
            for i in x:
                if i !=None:
                    summary+=i 
            return summary 

        def count_nonzero(x):
            count = 0
            for i in x:
                if i !=None:
                    count+=1 
            return count 
        for i in range(num_row):
            for j in range(num_column):
                value_list = [get_value(x,i,j), \
                              get_value(x,i-1,j),get_value(x,i+1,j),\
                              get_value(x,i,j-1), get_value(x,i,j+1), \
                              get_value(x,i+1,j+1),get_value(x,i-1,j-1), \
                              get_value(x,i+1,j-1) , get_value(x,i-1,j+1)]
                y[i][j]  = sum_nonzero(value_list)//count_nonzero(value_list)
        return y

