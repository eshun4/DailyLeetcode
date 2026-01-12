"""
1266. Minimum Time Visiting All Points

Easy

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
 

Example 1:


Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5
 

Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""

from typing import List

class Solution:
    
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # get the length of n
        n = len(points)
        # base case if you dont move anywhere 
        if n == 1:
            return 0 

        # create a distance tracker
        distance = 0

        # iterate through points
        for i in range(0, n-1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            dy = abs(y2 - y1)
            dx = abs(x2 - x1)
            distance += max(dx, dy)
        # return distance
        return distance


def main():
    solution = Solution()
    test_cases = [
    ([[1,1],[3,4],[-1,0]], 7),
    ([[3,2],[-2,2]], 5),
    ([[1,1]], 0),
    ([[0,0],[1,1]], 1),
    ([[0,0],[1,0],[1,1]], 2),
    ([[0,0],[10,10]], 10),
    ([[-5,-5],[5,5]], 10),
    ([[0,0],[3,4],[6,8]], 8),          # fixed
    ([[1,1],[2,2],[3,3],[4,4]], 3),
    ([[-1000,1000],[1000,-1000]], 2000) # fixed
]

        
    for points, expected in test_cases:
        got = solution.minTimeToVisitAllPoints(points)
        print(f"Input: {points} | Expected: {expected} | Got: {got} | {'✓' if got == expected else '✗'}")

if __name__ == "__main__":
    main()