# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #traverse list, put nodes in list, treat as stack
        node_stack = []
        current = head
        while current.next != None:
            node_stack.append(current)
            current = current.next
            
        #pop from list, define relationships between nodes
        head = current
        while node_stack != []:
            current.next = node_stack.pop()
            current = current.next
        current.next = None
        return head   