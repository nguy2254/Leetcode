# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
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
