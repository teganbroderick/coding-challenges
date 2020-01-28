# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        #start at head
        current = head
        
        if current == None:
            return None
        
        while current != None:
            #if head is the node to remove, 
            if current.val == val:
                #reassign head to head.next
                head = current.next
            
            #traverse the ll
            #if we get to the last node
            if current.next == None:
                break
            
            #if current.next is node to remove    
            if current.next.val == val:
                #if node to remove is not the last node in the list
                #reassign current.next to current.next.next
                if current.next.next != None:
                    current.next = current.next.next
                else:
                    #reassign current.next to none
                    #reassign tail of list to current node
                    current.next = None
                    tail = current
        
            current = current.next
            
        return head