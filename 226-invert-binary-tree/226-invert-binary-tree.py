# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap the children root
        tmp = root.left #save left root in temporary variable
        root.left = root.right #swap left and right root
        root.right = tmp # left root = right root
        
        self.invertTree(root.left) 
        self.invertTree(root.right) # call recursively to all roots
        return root