"""
865. Smallest Subtree with all the Deepest Nodes

Medium

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
Example 2:

Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.
Example 3:

Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
 

Constraints:

The number of nodes in the tree will be in the range [1, 500].
0 <= Node.val <= 500
The values of the nodes in the tree are unique.
 

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""
from typing import Optional
import time
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # do a post order traversal
        def post_order(root):
            # max depth 
            max_depth = float("-inf")
             # max_depth of subtree
            subtree_maxdepth = {}
            result = None
            # use a stack
            stack = [(root, 0, 0)]
            # check if root node is none
            if not root:
                return 0 
            
            while stack:
                node, depth, visited_count = stack.pop()
                if visited_count == 0:
                    # if not left node and right node
                    if not node.left and not node.right:
                        if depth > max_depth:
                            max_depth = depth

                    stack.append((node, depth, 1))

                    if node.right:
                        stack.append((node.right, depth + 1, 0))
                    if node.left:
                        stack.append((node.left, depth + 1, 0))
                    
                    

                elif visited_count == 1:
                    l_max = subtree_maxdepth.get(node.left, depth)
                    r_max = subtree_maxdepth.get(node.right, depth)
                    subtree_maxdepth[node] = max(l_max, r_max)
                    if l_max == r_max == max_depth:
                        result = node

            return result

        return post_order(root)

def serialize_tree(node):
    """Convert tree to level-order list representation"""
    if not node:
        return []
    result = []
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        if curr:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def main():
    test_cases = [
        (TreeNode(1), [1]),
        (TreeNode(1, TreeNode(2, TreeNode(3))), [3]),
        (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), [3]),
        (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),
         [1, 2, 3, 4, 5, 6, 7]),
        (TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                  TreeNode(1, TreeNode(0), TreeNode(8))),
         [2, 7, 4]),
        (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3)), [5]),
        (TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4, None, TreeNode(5)))), [5]),
        (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5))),
         [1, 2, 3, 4, None, None, 5]),
        (TreeNode(0, TreeNode(1, None, TreeNode(2)), TreeNode(3)), [2]),
        (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                  TreeNode(3, None, TreeNode(6, None, TreeNode(8)))),
         [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]),
    ]

    start = time.perf_counter()

    all_pass = True
    for i, (root, expected) in enumerate(test_cases, 1):
        result = Solution().subtreeWithAllDeepest(root)

        input_list = serialize_tree(root)
        output_list = serialize_tree(result)

        if output_list != expected:
            all_pass = False

        print(f"Case {i}")
        print("Input")
        print("root =")
        print(input_list)
        print("Output")
        print(output_list)
        print("Expected")
        print(expected)
        print()

    end = time.perf_counter()
    runtime_ms = int((end - start) * 1000)

    if all_pass:
        print("Accepted")
        print(f"Runtime: {runtime_ms} ms")
    else:
        print("Wrong Answer")
        print(f"Runtime: {runtime_ms} ms")

if __name__ == "__main__":
    main()
