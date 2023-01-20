# Link(s): #https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743457252_5Unit
# https://leetcode.com/problems/3sum-closest/description/

"""
Question:

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
"""

"""
Sample I/O:

Input: [-2, 0, 1, 2], target=2

Output: 1

Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
----------------------------
Input: [0, 0, 1, 1, 2, 6], target=5

Output: 4

Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0,0, 6]. Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4' which is less than the sum of the other triplet which is '6'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
"""

# Code goes here
def threeSumClosest(nums, target):
    nums.sort()
    numsLength = len(nums) - 1
    lowestSum = float("inf")
    for i in range(0, numsLength):
        firstNum = nums[i]
        remainingSum = target - firstNum
        first = i + 1
        last = numsLength 
        while first < last:
            secondNum = nums[first]
            thirdNum = nums[last]
            currentSum = secondNum + thirdNum
            if currentSum == remainingSum:
                return target
            if abs(target - firstNum - currentSum) < abs(target - lowestSum):
                lowestSum = firstNum + currentSum
            if currentSum < remainingSum:
                if firstNum + currentSum < lowestSum:
                    lowestSum = firstNum + currentSum
                first += 1
            else:
                last -= 1
    return lowestSum

"""
TC: O(N^2) | SC: O(N) # Required for sorting

Explanation:
We use a very similar approach here to the "Triple Sum to Zero" or "3Sum" problem where we were given an unsorted array and we needed
to find all triplets whose sum was equal to zero.

Using a trivial approach, we would need 3 nested loops -> O(N^3) TC.

However, we can sort this array and then use a two pointer approach to reduce one nested loop.
We do this by using the two pointer approach to find a target sum of two elements using a single run.

1. Sort the array (Note/Reminder: two pointer approach only works on sorted arrays)
2. Iterate through each element of the array
3. For each element in the outer loop, calculate the remaining sum needed to reach the target.
4. Set left pointer to the next element of i, and right pointer at the last element of the sorted array.
5. Use the two pointer approach to move around the pointers to get closest to the required remaining target sum.
6. If the current sum of two elements is equal to that required sum, return the target sum itself.
7. Otherwise, check if the current lowest sum being tracked is closer to the target sum vs the sum of the current element pair.
8. Swap the lowest sum if needed and keep moving the pointers left and right.
9. Return the lowest sum.
"""