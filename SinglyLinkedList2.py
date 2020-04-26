# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None  
        else:
            fast = slow  = head 
            while fast and fast.next: 
                slow = slow.next
                fast = fast.next.next 
                if slow  == fast: 
                     break 
            else:
                return None
            while head != slow: 
                slow = slow.next
                head = head.next 
         #Hashtable 
        if headA is None: return None  
        else:
            hashtable = set()
            while headA: 
                length = len(hashtable)
                hashtable.add(headA)
                headA = headA.next
            while headB: 
                length = len(hashtable)
                hashtable.add(headB)
                if length == len(hashtable):
                    return headB
                headB = headB.next
            return None            return head 
        #Hashtable 
        if headA is None: return None  
        else:
            hashtable = set()
            while headA: 
                length = len(hashtable)
                hashtable.add(headA)
                headA = headA.next
            while headB: 
                length = len(hashtable)
                hashtable.add(headB)
                if length == len(hashtable):
                    return headB
                headB = headB.next
            return None 
        #Two pointers 
        #Two pointers 
        pointA = headA
        pointB = headB
        while pointA is not pointB:
            if pointA is None: 
                pointA = headB 
            else: 
                pointA = pointA.next
            if pointB is None: 
                pointB = headA 
            else: 
                pointB = pointB.next
        return pointA
