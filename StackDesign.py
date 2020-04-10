class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue =[] 
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #If blank, append x
        if not self.queue: self.queue.append(x)
        #If not blank, append the min of x and the last value 
        else: self.queue.append(min(x,self.queue[-2]))
        #Append x into the queue 
        self.queue.append(x)
        
    def pop(self):
        """
        :rtype: None
        """
        #When pop, pop out both the minimum value and itself
        self.queue.pop()
        self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.queue: return self.queue[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.queue: return self.queue[-2]
        


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue =[] 
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        currMin = self.getMin()
        if currMin is None or x < currMin: currMin = x
        if not self.queue: self.queue.append((x,x))
        else: self.queue.append((x,currMin))
        
    def pop(self):
        """
        :rtype: None
        """
        #When pop, pop out both the minimum value and itself
        self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.queue: return self.queue[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.queue: return self.queue[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
