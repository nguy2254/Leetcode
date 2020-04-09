class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head or head.next is None:
            return None
        
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next 
        current = head 
        mid = length // 2 
        for i in range(mid): current = current.next
        return current 
