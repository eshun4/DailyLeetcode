"""
1390. Four Divisors

Medium

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
"""


import math 
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        # iterate through the numbers
        for num in nums:
            # use set to keep track of divisors
            divisors = set()
            # iterate from 1 to sqrt of num 
            for j in range(1, int(math.sqrt(num)) + 1):
                if num % j == 0:
                    divisors.add(j)
                    divisors.add(num // j)
                    # early termination clause
                    if len(divisors) > 4:
                        break
                
            if len(divisors) == 4:
                total += sum(divisors)
        return total

        


def main():
    test_cases = [
        ([21, 4, 7], 32),
        ([21, 21], 64),
        ([1, 2, 3, 4, 5], 0),
        ([6], 12),
        ([10], 18),
        ([15], 24),
        ([100], 0),
        ([6, 10, 15], 54),
        ([1], 0),
        ([2, 3, 5, 7], 0),
    ]
        
    solution = Solution()
    for nums, expected in test_cases:
        result = solution.sumFourDivisors(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} nums={nums}, expected={expected}, got={result}")

if __name__ == "__main__":
    main()