# PROBLEM STATEMENT

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

# EXAMPLE

    Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Output: [[1,2],[1,4],[1,6]]

Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# **1. BRUTE FORCE SOLUTION WITH SORTING - MEMORY LIMIT EXCEEDED**

Without thinking of any optimization in mind, the most straightforward way would be to get every single pair possible and then sort all the pairs by their sums, and then return the "k" smallest pairs.

But, since both the lists can have lenghts of up to 10^5, it means, in worst case, we will have 10^5 * 10^5 pairs that we have to sort. That's why, this solution will give Memory Limit Exceeded error for large test cases.

So, from this, we can understand one thing - We don't have to care about every single pair. We just want "k" smallest pairs.     


# **2. BRUTE FORCE SOLUTION WITH MAX HEAP - TIME LIMIT EXCEEDED**

So, now that sorting solution failed, another thing we can try is to just care about "k" pairs at any time. And so, we want a data structure that automatically orders elements withous us having to sort each time. And that data structure is a heap. In this problem, we will use a maxHeap because we want the "k" smallest pairs so a maxHeap will have the smallest on the bottom and the pair with the maximum sum on the top. So, we can easily remove the pairs with a bigger sum value from top.

And at any time, we will maintain the size of the heap as "k". This will ensure we don't get a Memory Limit Exceeded issue.

But, now the issue is this will still fail for large test cases. Because, basically what we are writing is an O(N^2) time solution because while we have solved the memory issue, we are still going over every single pair. 

# **3. OPTIMIZED BRUTE FORCE SOLUTION WITH MAX HEAP - ACCEPTED**

There is a reason why the problem says both the lists are "Sorted in non-decreasing order". In other words, both lists are sorted in increasing order.

What this means is, there will be a point after which, no new pair will give us a smaller sum than the ones in the maxHeap. 

For example, if we have nums1 = [1,7,11], nums2 = [2,4,6], k = 3

	We start with the first element in nums1 -> "1"
	
	Now, we loop over every single element in nums2.
	
	First, we get "2" so pair is (1,2).  
	
	So, we push a triplet into maxHeap -> [sum,nums1 element, num2 element]
	
	So, we push [3,1,2] into the maxHeap
	
	Next, we have "4" in nums2. So, pair is (1,4) and we push [5,1,4] in maxHeap
	
	Next, we have "6" in num2, so pair is (1,6) and we push [7,1,6] in maxHeap
	
	Now, we need only "3" pairs and the maxHeap already has "3" triplets in it.
	
	Since it is a maxHeap, it means, the pair on top current has the highest sum.
	
	So, whatever new pair comes, we can simply compare its sum to this top pair.
	If the new pair has a smaller sum, we can replace the top.
	
	For example, the next element in nums1 is "7"
	
	And so, we go over each element in nums2 again.
	
	First, we have "2" and so pair is (7,2) and its sum is "9".
	
	Now, we see that the maximum sum in heap right now is "7"
	This means, the current pair has a higher sum than the highest in maxHeap.
	
	And this also means, not only this pair, 
	but every pair that comes next will have a higher sum than top of maxHeap
	
	And so, it makes no sense to go over all those pairs.
	
	And since we already have "k" pairs in maxHeap, we can simply break and return them.
	
And that's the optimization that we can add to our Brute Force solution and this solution be accepted.

