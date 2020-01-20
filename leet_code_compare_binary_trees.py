# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """return true is trees are the same"""
        
        def traverse_tree(treenode):
            """traverse tree, return array containing tree node values"""
            
            
            to_check = [treenode]
            node_list = [treenode]
            
            while to_check != []:
                current = to_check.pop(0)
                if current != None:
                    left = current.left
                    right = current.right

                    node_list.append(left)
                    node_list.append(right)

                    to_check.append(left)
                    to_check.append(right)
            
            return node_list
                
        list_p = traverse_tree(p)
        list_q = traverse_tree(p)
        
        if list_p == list_q:
            return True
        else:
            return False