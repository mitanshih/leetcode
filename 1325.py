
'''1325. Delete Leaves With a Given Value
Created on 2024-05-25 17:23:41
2024-05-25 18:59:34

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional


#%%    Variable
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#%%    Functions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int
                        ) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # `root.val == target` is the most important condition.
        if root.val == target and root.left is None and root.right is None:
            return None
        return root

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
