class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def stringToListNode(numbers):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class Solution(object):
    def middleNode(self,head):
        if head is None: return None 
        length =1
        current = head 
        while current is not None:
            length = length + 1 
            current = current.next 
        mid = length //2 
        current = head 
        for i in range(mid):
            current = current.next 
        return current

    def middleNode2(self,head):
        if head is None: return None
        slow = fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow



