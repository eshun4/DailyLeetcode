"""
961. N-Repeated Element in Size 2N Array

Easy

You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
 

Constraints:

2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""

from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # create a counter hashmap
        counter ={}
        # get the length of the array 
        n = len(nums)
        # get the reallength of n
        real= n // 2
        # count the number of elements in the array
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            # if the count is equal to real return the num 
            if counter[num] == real:
                return num
        

def main():
    test_cases = [
        ([1, 2, 3, 3], 3),
        ([2, 1, 2, 5, 3, 2], 2),
        ([5, 1, 5, 2, 5, 3, 5, 4], 5),
        ([1, 1], 1),
        ([0, 0, 0, 1], 0)
    ]

    for nums, expected in test_cases:
        result = Solution().repeatedNTimes(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums} -> Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    main()