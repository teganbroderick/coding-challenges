# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """return num of nodes along the shortest path from the root node down to the nearest leaf node"""
    
        if root == None:
            return 0

        to_check = [(root, 0)]
        depth_set = set()

        while to_check != []:
            #pop current and depth from stack
            current, depth = to_check.pop()
            # print(current, depth)
            
            if current.left != None:
                to_check.append((current.left, depth+1))
                if depth + 1 not in depth_set:
                    depth_set.add(depth + 1)
            
            if current.right != None:
                to_check.append((current.right, depth+1))
                if depth + 1 not in depth_set:
                    depth_set.add(depth + 1)
            
            # print(to_check)
            # print(depth_set)
            
            
        if len(depth_set) == 0:
            return 0
        else:
            min_depth = max(depth_set)
            return min_depth
            
            
            
            
            
        
        
        