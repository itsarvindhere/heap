# PROBLEM STATEMENT

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

 - The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
 - It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).

Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

# EXAMPLE

    Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
    Output: 12

Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.

# APPROACH

To understand the solution easily, we can divide the problem into sub-problems.

It is given that for chosen indices i0, i1, ..., ik - 1, the score is defined as: 

	The sum of the selected elements from nums1 
	multiplied with the minimum of the selected elements from nums2.
	
So, we have two things to take care of in this problem - 

	1. We want to find the sum of elements of a subsequence in nums1
	2. We want the find the minimum of elements of a subsequence in nums2

And we want to have an efficient way to do both these things. A Brute Force approach will fail due to the constraints.

Let's think of the second sub-problem first. We want the minimum element in a subsequence. So, we can use sorting here because if we sort nums2 in decreasing order, then for any subsequence that ends at an index "i", the minimum element will always be nums2[i] since nums2 is sorted.

	That is, if we have nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
	
	If we sort nums2 in decreasing order -> nums2 = [4,3,2,1]
	
	So, if a subsequence ends at index 2, then minimum is nums2[2] => 2
	If a subsequence ends at index 3, then the minimum is nums2[3] => 1
	
	But, since we sorted nums2, num1's elements also need to be arranged accordingly
	
	That's why, we won't sort nums2 alone but first we will combine both the lists
	
	nums = [(1,2), (3,1), (3,3), (2,4)]
	
	So now, each pair at index "i" in nums is like this => (nums1[i], nums2[i])
	
	And now we can sort this combined list based on the nums2 data in decreasing order
	
	nums = [(4,2), (3,3), (1,2), (3,1)]
	
So, our second sub-problem is now solved as we can now efficiently get the smallest element in a subsequence ending at index "i".

But what about the first sub-problem of finding the sum?

	Let's take the same example. 
	So far, nums = [(4,2), (3,3), (1,2), (3,1)]
	
	We want a subsequence to be of length "k"
	Suppose, we are checking the subsequence ending at index 3
	
	So, for a subsequence ending at index 3, minimum = nums[3][1]
	
	And what about sum? We cannot just go over every single subsequence ending at index 3 and get its sum
	Since we want to maximize the overall subsequence score, 
	we want the maximum subsequence sum for a subsequence that ends at index 3
	
	As we have already considered index 3, we have already found one element of subsequence.
	And so, we want the rest k - 1 other elements for this subsequence.
	It is also pretty obvious that since this subsequence ends at index 3,
	the rest k - 1 elements will be on the left side of index 3.
	
	And since we want to maximize this sum, we want the maximum k - 1 elements on left side of index 2.
	
Now you should've got a hint of what approach to take to find the maximum k - 1 elements till a particular index.

We will use a minHeap here to get the top k -1 elements at any time for any subsequence ending at index "i"

We also want to maintain the current subsequence sum to avoid having to write a nested loop to get the sum from the heap.

So, as we push a new element to the minHeap, it will have to remove the smallest element from it so that its size remains k only.

So, whatever element it removes, that will also be reduced from the current subsequence sum. And whatever element we push to the heap, that will be added to the current subsequence sum. In this way, we can maintain the subsequence sum easily.
	
And finally, we just want to update the maximum score in each iteration and return it at the end.