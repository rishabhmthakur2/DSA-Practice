# Link(s): https://leetcode.com/problems/two-sum/

"""
Question:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

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
    visitedNums = {}
    for i in range(0, len(nums)):
        num = nums[i]
        remainder = target - num
        if remainder in visitedNums:
            return [i, visitedNums[remainder]]
        else:
            visitedNums[num] = i

"""
TC: O(N) | SC: O(N)

Explanation:

Using brute force, this problem would require N^2 operations as we will match each element with the remaining elements to find if the target pair exists.
If the array was sorted, we could have just used the Two Pointer approach which would have given us a solution with a TC of O(N) and SC of O(1).

However, since the array is not sorted, we will have to go through each element one by one but find a way to find the pair in a single run.
To do this, we would store the list of elements we have already seen in the array in a dictionary.

Within our run, for each element, we see if the other number for this element is there in the dicitionary. If it is present, we return the indices of the two elements.
If it is not, we add the current element into the dictionary for future checks.
"""

