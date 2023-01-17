# Two-pointer approach

For questions where we have a _sorted array_ or a _linked list_ and the task is to find a set of elements that fulfill a given condition, the usual way is to consider all elements one by one.

Take the following example: Given an array of sorted numbers and a target sum, find a pair in the array whose sum matches the target sum.
For the question above, we can loop through our array in a nested manner, considering all elements with first element and then the second element and so on. This gives us a complexity of O(N^2).

However, since the array is already sorted, we can use that to our advantage. We use two pointers, one mostly from the start of the array and another one from the end and we craft our algorithm in such a way that we move the two pointers towards the middle under different scenarios to find a solution). 

For the question above, consider the following algorithm:
1. If the sum of elements at the first pointer and the last pointer is less than the sum, move the first pointer to the right.
2. If the sum is greater than the target sum, move the last pointer to the left.
3. If the sum is equal to the target sum, we have our pair. Return the indices.

The above algorithm allows us to find the solution (if it exists) in one run - giving us a time complexity of O(N).

In case of Linked Lists, we usually use the two pointers or the slow and the fast pointers to solve questions like - Is there a cycle in the Linked List, common elements in two Linked Lists.