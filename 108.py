
'''108. Convert Sorted Array to Binary Search Tree
Created on 2024-05-25 18:14:03

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional

#%%    Variable
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
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def add_middle_to_TreeNode(left: int, right: int
                                   ) -> Optional[TreeNode]:
            if left > right:
                return None
            middle_index: int = left + (right - left) // 2
            root: TreeNode = TreeNode(nums[middle_index])
            root.left = add_middle_to_TreeNode(left, middle_index - 1)
            root.right = add_middle_to_TreeNode(middle_index + 1, right)

            return root
        return add_middle_to_TreeNode(0, len(nums) - 1)

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
