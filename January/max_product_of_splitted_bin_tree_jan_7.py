"""
1339. Maximum Product of Splitted Binary Tree

Medium

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""

from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        # get results 
        result = 0
        subtree_sum = {}
        
        # create a recursive dfs in order sum getter
        def postorder_sum(root):
            if not root:
                return 0
            left = postorder_sum(root.left)
            right = postorder_sum(root.right)
            total =  root.val + left + right 
            subtree_sum[root] = total
            return total

        total = postorder_sum(root)
        # iterate through the dict and get the products of the total - each sub tree times the subtree itself
        for key, value in subtree_sum.items():
            complement = total - value
            curr_product = (value) * (complement)
            if curr_product > result:
                result = curr_product
        # return the maximum of the result modulo mod
        return result % MOD



def build_tree_leetcode(level_order) -> Optional[TreeNode]:
    """Builds a binary tree from LeetCode level-order list representation."""
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    q = deque([root])
    i = 1

    while q and i < len(level_order):
        node = q.popleft()

        # left child
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            q.append(node.left)
        i += 1

        # right child
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            q.append(node.right)
        i += 1

    return root

def main():
    test_cases = [
        ([1,2,3,4,5,6], 110),
        ([1,None,2,3,4,None,None,5,6], 90),  # LeetCode example 2
        ([2,1], 2),
        ([1,1,1,1,1,1,1], 12),
        ([10,5,8,3,2,6,4], 360),
        ([100,50,50], 7500),
        ([1,1,1,1,1], 6),
        ([15,10,20,5,5,10,10], 1400),
        ([7,3,4,2,1,6], 130),
        ([20,10,10,5,5,5,5], 800),
    ]

    for arr, expected in test_cases:
        root = build_tree_leetcode(arr)
        got = Solution().maxProduct(root)
        status = "✓" if got == expected else "✗"
        print(f"{status} Input: {arr} -> Expected: {expected}, Got: {got}")

if __name__ == "__main__":
    main()