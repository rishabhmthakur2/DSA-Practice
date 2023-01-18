# Link(s): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743435284_3Unit
# https://leetcode.com/problems/squares-of-a-sorted-array/

"""
Question:
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

"""

"""
Sample I/O:

Input: [-4,-1,0,3,10]

Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
----------------------------
Input: [-7,-3,2,3,11]

Output: [4,9,9,49,121]

Explanation:
"""

# Code goes here

def sortedSquares(nums):
    if len(nums) == 1:
            return [nums[0]**2]
    result = []
    first = 0
    while nums[first] < 0 and first < len(nums) - 1:
        first += 1
    first = first - 1
    last = first + 1
    while first > -1 and last < len(nums):
        firstNum = abs(nums[first])
        lastNum = abs(nums[last])
        if firstNum < lastNum or last == len(nums):
            result.append(firstNum ** 2)
            first -= 1
        else:
            result.append(lastNum ** 2)
            last += 1
    if first == -1:
        while last < len(nums):
            result.append(nums[last]**2)
            last += 1
    else:
        while first > -1:
            result.append(nums[first]**2)
            first -= 1
    
    return result

"""
TC: O(N) | SC: O(N) # We use the result array of size N

Explanation:
The trivial approach would be to square each element first in one run and then sort the squared array. However, the sorting at the end would be an 
O(NlogN) operation.

An optimal solutions would be to use the "Two Pointer" approach since the array is already sorted. Note that the only tricky part about this question is the presence of negative elements.

We start with finding the index of the first negative element. We then place one pointer at this number and the other pointer to the number on its right.

-7, -3, -1, 1, 9, 23
        ^   ^
        |   |
        F   L

Now, we check the absolute values for the numbers on both pointers. We square the number with the lower absolute value and then store it as the first element.
If the smaller number was negative, we move the F pointer to left by 1 else we move the L pointer to right by 1.

We repeat this till we have covered all elements.
"""