# Link(s):
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743424499_2Unit

"""
Question:

Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.
"""

"""
Sample I/O:

Input: [2, 3, 3, 3, 6, 9, 9]

Output: 4

Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
----------------------------
Input: [2, 2, 2, 11]

Output: 2

Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

# Code goes here
def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        first = 0
        last = first + 1
        uniqueCount = 1
        while last < len(nums):
            firstNum = nums[first]
            lastNum = nums[last]
            if firstNum != lastNum:
                uniqueCount += 1
                if last == first + 1:
                    last += 1
                else:
                    nums[first + 1] = lastNum
                first += 1
            else:
                last += 1
        return uniqueCount

"""
TC: O(N) | SC: O(1)

Explanation:
The brute force mechanism would have been to run via each element and see if another element with the same number exists.
If it does, we can replace that duplicate with a unique character or an infinte number.
We can then sort the array and return it. This would lead in a TC of O(N^2).

However, we can use the two pointer approach to maintain two pointers and check two elements against one another in a single run.
Since the array is already sorted, this approach makes a lot of sense as repeated elements will always be together.

1. We start with a first pointer at index 0 and a second pointer at index 1. We then check the elements as these two indices.

2. If the two elements are same, we then move the last pointer by 1 to the right in search of the next unique element.

3. If the two elements are different, we check if the two elements lie next to each other.
    3.a. If they do, that means they are already in their right positions and don't need any swaps. We just move the first and the last pointers to the right by 1.
    3.b. If the elements are not next to each other, that means that their are duplicate elements of the first pointer between them.
        3.b.1. We then replace the element at first + 1, which is the first duplicate element with the element at the last pointer and move first to this newly swapped pointer to look for the next element or its duplicates.
        3.b.2. We maintain a variable to count the number  of unique elements. This counter can be appended by 1 whenever we make a swap of numbers.
"""