# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
    
        to_check = [root]
        node_list = []
        
        while to_check:
            current = to_check.pop()
            node_list.append(current.val)
            #need to check left side first
            #add right child first so that left child gets popped off first
            if current.right != None:
                to_check.append(current.right)   
            
            if current.left != None:
                to_check.append(current.left)
            
        return node_list