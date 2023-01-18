# Link(s): https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743445291_4Unit
# https://leetcode.com/problems/3sum/description/

"""
Question:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

"""
Sample I/O:

Input: [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
----------------------------
Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.
"""

# Code goes here
def threeSum(nums):
    nums.sort()
    results = []
    for i in range(0, len(nums)): # Iterate over the array
        firstNum = nums[i]
        if i > 0:
            if firstNum == nums[i-1]:
                continue # Keep moving forward if there are duplicates
        targetSum = 0 - firstNum # Calculate target sum for the remaining numbers
        left = i + 1 # Left Pointer
        right = len(nums) - 1 # Right Pointer
        while left < right: # Two sum approach
            secondNum = nums[left]
            thirdNum = nums[right]
            currentSum = secondNum + thirdNum
            if currentSum == targetSum:
                result = [nums[i], nums[left], nums[right]]
                results.append(result)
                left += 1
                while left < right and left > 0 and nums[left] == nums[left - 1]: 
                    left += 1 # Keep moving if duplicate elements
                right -= 1
                while left < right and right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right += 1 # Keep moving if duplicate elements
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return(results)

"""
TC: O(N^2) | SC: O(N) # Required while sorting the array

Explanation:
The greedy approach would be to use three nested loops and then find elements that sum up to 0.
However, we can find a better and optimal solution for it.

If we think about breaking this problem down, we quickly can think of how we can inculcate the Two Sum problem in this question.
In the two sum problem, we find pairs that add up to a target sum (which in this case is 0) and in this case we are looking at triplets.

So a better approach could be to use the two sum approach for each element. Aka for each element in the array, we find the two other elements
that match the required sum (0 - currentElement). 
This gives us a time complexity of O(N^2) - We have an outer loop that goes through each element. And then we have an inner loop that uses the O(N) two sum approach of finding pairs.

The tricky part of this question is to remove duplicate triplets. Since our array is sorted, the duplicate numbers will be next to each other.
Hence, we can continue moving our pointers in the two loops whenever there are duplicate numbers so that we only calculate triplets using unique numbers.
"""