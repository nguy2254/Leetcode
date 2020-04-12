class Solution(object):
    def reverseList(self, head):
        if head is None: return None
        point_prev = None 
        point_current = head 
        while point_current: 
            point_next  = point_current.next 
            point_current.next = point_prev
            point_prev = point_current
            point_current = point_next 
        return point_prev 
