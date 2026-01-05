"""
1975. Maximum Matrix Sum

Medium


You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
"""
from typing import List 

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # find abs sum of all numbers in matrix 
        abs_sum, smallest_abs_number, count_of_neg = 0, abs(matrix[0][0]), 0
        for row in matrix:
            for number in row:
                abs_sum += abs(number)
                if abs(number) < abs(smallest_abs_number):
                    smallest_abs_number = abs(number)
                if number < 0:
                    count_of_neg += 1
        if count_of_neg % 2 == 0:
            return abs_sum 
        return abs_sum - 2 * (smallest_abs_number)
    




        

def main():
    solution = Solution()
    test_cases = [
        ([[1, -1], [-1, 1]], 4),
        ([[1, 2, 3], [-1, -2, -3], [1, 2, 3]], 16),
        ([[1]], 1),
        ([[-1, -2], [-3, -4]], 10),
        ([[5, -5], [-5, 5]], 20),
        ([[0, 1], [1, 0]], 2),
        ([[-1], [-1]], 2),
        ([[100, -100], [100, -100]], 400),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 136),
        ([[-10, 20, -30], [40, -50, 60], [-70, 80, -90]], 430),
    ]
    
    for i, (matrix, expected) in enumerate(test_cases):
        result = solution.maxMatrixSum(matrix)
        status = "✓" if result == expected else "✗"
        print(f"Test {i+1}: {status} Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    main()