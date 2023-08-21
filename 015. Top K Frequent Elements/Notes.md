# PROBLEM STATMENT

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# EXAMPLE

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

# BUCKET SORT APPROACH

The sorting and heap approaches are pretty simple to understand. But the main thing is to understand how the Bucket Sort approach works.

If the comments are not clear, here is an example.

	Take nums = [1,1,1,2,2,3], k = 2

	We know that since there are 6 values in this list, each value will occur at least 1 time or at most "6" times
	
	So, the frequency will be between 1 and 6 (both included)
	
	And so, we can use bucket sort such that each bucket holds elements with same frequency.
	
	So, for this example, we will have a list of length = n, where each index = frequency
	
	For example, we will have a list of length 6 for above example, initially having empty buckets
	
	[ [], [], [], [], [], [] ]
	
	Here, 
	index 0 represents frequency 1
	index 1 represents frequency 2
	.
	.
	.
	index 5 represents frequency 6
	
	
	So now, we can take the frequency of each element from a hashmap and put that element in correct bucket.
	
	In above example, hashmap will be - 
	
		{ 1 : 3, 2 : 2, 3: 1}
		
	So it means, element "1" with frequency = 3, will go in bucket at index = 2 (0 based indexing)
	And so on..
	
	So eventually, our list now becomes [ [3], [2], [1], [], [], [] ]
	
	And as you might have expected, now we can iterate over this list from right to left 
	and take the "k" elements and put them in output list.
	
And finally, just return that output list.