class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None 
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if not self.head: return -1
        else: 
            if index == 0: return self.head.val 
            else:
                count = 0
                current = self.head 
                while current:
                    if count == index: return current.val
                    count = count + 1
                    current = current.next
                return -1      
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        current = Node(val) 
        current.next = self.head 
        self.head = current 


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None: 
            self.head = Node(val)
        else: 
            previous = self.head 
            while previous.next is not None:
                previous = previous.next 
            previous.next = Node(val) 

        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        node = Node(val) 
        if self.head is None: 
            self.head = node 
        if index == 0: 
            current = Node(val) 
            current.next = self.head 
            self.head = current
        else:
            count = 0
            current = self.head
            while current is not None:
                count = count +1 
                if count == index:    
                    node.next  = current.next
                    current.next = node  
                current = current.next

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if self.head is None: return 

        # Store head node 
        temp = self.head 
  
        # If head needs to be removed 
        if index == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(index -1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
  
        temp.next = next 
             
            

                         


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
