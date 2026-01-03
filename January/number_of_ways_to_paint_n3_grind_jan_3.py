"""
1411. Number of Ways to Paint N × 3 Grid

Hard

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: 
Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000

"""


class Solution:
    def numOfWays(self, n: int) -> int:
        pass 
    
    
    
def main():
    Solution().numOfWays()
    test_cases = [
                (1, 12),
                (2, 54),
                (3, 246),
                (4, 1080),
                (5, 30228214),
                (6, 139536240),
                (7, 646990950),
                (8, 505821150),
                (9, 879667360),
                (10, 828172140),
            ]

    for n, expected in test_cases:
        result = Solution().numOfWays(n)
        print(f"n={n}: {result} (expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")


if __name__ == "__main__":
    main()
            