"""
1161. Maximum Level Sum of a Binary Tree

Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""

from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # check if the rrot is None
        if not root:
            return []
        #create a quee for the elements and append the root
        my_queue = deque([(0, root)])
        # level and sum map
        level_sum = {}
        # get the best sum
        best_sum = float("-inf")
        # iterate while queue is nto empty
        while my_queue:
            level_size = len(my_queue)
            # keep track of nodes at each level
            lev_sum = 0
            # iterate through each level
            for _ in range(level_size):
                # get current level and node
                curr_level, curr_node = my_queue.popleft()
                # append values to level vals array
                lev_sum += curr_node.val
                # logic of BFS
                if curr_node.left:
                    my_queue.append((curr_level + 1, curr_node.left))
                if curr_node.right:
                    my_queue.append((curr_level + 1, curr_node.right))

            if lev_sum > best_sum:
                best_sum = lev_sum
            # use hashmap to keep track of level and sum
            level_sum[curr_level + 1] = best_sum
        # return max level based on the sum of the nodes
        return max(level_sum, key=level_sum.get)
        

        
        

def main():
    # Test cases for maxLevelSum
    test_cases = [
        # [1,7,0,7,-8,null,null] -> Expected: 2
        ([1,7,0,7,-8,None,None], 2),
        # [989,null,10250,98693,-89388,null,null,null,-32127] -> Expected: 2
        ([989,None,10250,98693,-89388,None,None,None,-32127], 2),
        # Single node
        ([5], 1),
        # All positive values
        ([1,2,3,4,5,6,7], 3),
        # All negative values
        ([-1,-2,-3,-4,-5,-6,-7], 1),
        # Two levels
        ([10,5,15], 1),
        # Unbalanced tree (left skewed)
        ([1,2,3,4,5], 2),
        # Unbalanced tree (right skewed)
        ([1,None,2,None,3,None,4], 1),
        # Mixed positive and negative
        ([100,-50,75,-25,50], 1),
        # Large values
        ([100000,-100000,50000], 1),
    ]

    solution = Solution()
    for i, (root_arr, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: Expected {expected}")

if __name__ =="__main__":
    main()