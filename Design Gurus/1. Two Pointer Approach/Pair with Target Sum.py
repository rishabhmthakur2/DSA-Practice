"""
Link(s): 
https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743417172_1Unit
"""

"""
Question:
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

"""

"""
Sample I/O:

Input: array = [1, 2, 3, 4, 6]; target = 6

Output: [1,3]

Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
----------------------------
Input: array = [2, 5, 9, 11]; target = 11

Output: [0,2]

Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""
# Code goes here

# Unoptimized code - Brute Force - O(N^2)
def TwoSumUnoptimized(nums, target):
    numsLength = len(nums)
    for i in range(0, numsLength):
        for j in range(i+1, numsLength):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimized code - Two pointer approach
def TwoSum(nums, target):
    first = 0
    last = len(nums) - 1
    while first < last:
        firstNum = nums[first]
        lastNum = nums[last]
        if firstNum + lastNum == target:
            return [first, last] # We have a match
        if firstNum + lastNum < target:
            first += 1 # Sum was less, that means we need a bigger number, moving to the next bigger number in the array
        else:
            last -= 1 # Sum was larger, that means we need a smaller number, moving to the next smallest number in the array.
    return [-1, -1] # No result found

"""
TC: O(N) | SC: O(1)

Explanation:

Using brute force, this problem would require N^2 operations as we will match each element with the remaining elements to find if the target pair exists.
However, since the array is already sorted, we can take advantage of that and use the Two Pointer approach (refer to Readme of this folder).

We start by placing two pointers, one at the start - at the lowest element; another one at the end - at the biggest element.
We then compare the sum of these two elements with the target pait.
1. If the sum is same as target, we have a match. Return the indices.
2. If the sum is smaller than the target, that means we need a bigger number. We move the first pointer to the right as that is the next biggest number (array is sorted).
3. If the sum is greater than the targer, that means we need a smaller number and hence move the right pointer one step left.
"""

