# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        else:
            hashtable = set()
            while True: 
                if head is None: 
                    return False
                length = len(hashtable)
                hashtable.add(head)
                if length == len(hashtable):
                    return True 
                head = head.next
                
      def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        else:
            slow = fast = head
            while fast and fast.next:
                 fast = fast.next.next
                 slow = slow.next
                 if fast == slow:
                        return True
            return False 
