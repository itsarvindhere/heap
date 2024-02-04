# PROBLEM STATEMENT

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

    - For examples, if arr = [2,3,4], the median is 3.
    - For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
  
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

# EXAMPLE

    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]

Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6


# APPROACH

The core idea of this approach is same as **[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)**

You can understand that approach from this post of mine - https://leetcode.com/problems/find-median-from-data-stream/discuss/4598511/Python-2-Solutions-SortedList-and-Heap

Anyways, the main issue is not related to finding the median. In fact, the main issue in the Heap approach is - 

	How to Delete Elements that are no longer part of a Window?
	
We know that in a Heap, we can remove elements quickly and efficiently if and only if they are on the top. But, removal from somewhere between is not efficient and in the worst case, it is an O(N) time operation.

If you try to write a solution like that, you will probably get TLE. 

A better and more efficient approach is to do "LAZY DELETION".

What that means is, we will "ASSUME" that we have removed an element if it is no longer part of the current window. But, we will not remove it from the heaps unless it is at the top. This means, at a time, our heaps may have more elements than we need, just because the heaps also have those elements that we have "ASSUMED" as deleted.

And so, we cannot directly take the length of the heaps as simply "len(maxHeap" or "len(minHeap)". Because we also need to think of the fact that "maxHeap" or "minHeap" may also have those elements that have been removed already. 

And so, we will have separate variables, just to keep track of the lengths of the heaps, instead of using the "len()" function. We will update these variables whenever an element has to be removed, doesn't matter if we don't actually remove it at that time.

Finally, to keep track of the elements to be removed, we can use a dictionary which will have element as the key and its frequency as the value. Because note that the input list doesn't necessarily have unique elements.

And that's the whole idea. 