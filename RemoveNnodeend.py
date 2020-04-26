# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None: return None
        #Reverse time 1 
        prevPoint = None
        currentPoint = head 
        length =  1 
        while currentPoint:
            nextPoint = currentPoint.next 
            currentPoint.next = prevPoint
            prevPoint = currentPoint 
            currentPoint = nextPoint
            length = length + 1 
        #Delete at point n 
        temp = prevPoint
        if n == 1:
            prevPoint = temp.next
        if n == 2: 
            prevPoint.next = prevPoint.next.next 
        else: 
            for i in range(n-2): 
                if temp is not None: temp = temp.next
            if temp  and temp.next: 
                next = temp.next.next 
                temp.next = next                
        #Revers time 2
        prevPoint1 = None
        currentPoint1 = prevPoint 
        while currentPoint1:
            nextPoint1 = currentPoint1.next 
            currentPoint1.next = prevPoint1
            prevPoint1 = currentPoint1 
            currentPoint1 = nextPoint1  

        return prevPoint1 
            
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None: return None 
        slow = fast = head 
        for i in range(n):
            fast = fast.next 
        if not fast:  
            return slow.next 
        while fast.next: 
            slow = slow.next 
            fast = fast.next
        slow.next = slow.next.next  
        return head   
            
            
