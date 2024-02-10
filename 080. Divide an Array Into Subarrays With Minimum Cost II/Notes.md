# PROBLEM STATEMENT

You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.

# EXAMPLE

    Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
    Output: 15

Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.

It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.

# APPROACH

There are some things you need to understand before we go over the different solutions.

We need to divide the array into "k" subarrays and a valid division is the one where the difference between the starting index of second subarray and starting index of "kth" subarray is <= dist.

In other words, for a valid division, the distance between starting index of second subarray and starting index of last subarray <= k.

For any subarray, its cost is simply its first element. This also means that for the first subarray, the cost will always be the element at index 0. Because the first subarray will always have first element as the index "0" element. So, that's one thing which is the same for all test cases.

Next, let's talk about the second subarray.

If the first subarray will always have starting index as 0, it means, for the second subarray, the minimum starting index will always be "1". 

What about the maximum?

To understand that, let' take an example.

	nums = [10,1,2,2,2,1], k = 4, dist = 3
	
	k = 4 means we have to divide this array into four subarrays.
	
	For now, forget that "dist" exists.
	
	So, we know the minimum possible starting index for second subarray can be 1
	
	If "1" is the starting index, we can divide the array as - 
	
	[10], [1], [2], [2,2,1]
	
	Can "2" be the starting index of second subarray? YES.
	
	[10,1], [2], [2], [2,1]
	
	Can "3" be the starting index of second subarray? YES.
	
	[10,1,2], [2], [2], [1]
	
	Can "4" be the starting index of second subarray? NO!
	
	But why?
	
	That's because if second subarray starts with index "4",
	then we only have one element left after index "4"
	But, the number of subarrays yet to create are 2
	
	And since a subarray needs at least one element,
	we cannot start second subarray from index "4"
	
	This means, for this particular array and "k = 4",
	
	the maximum possible starting index for second subarray is "3"
	
	Or we can say,
	
	For any array with length "n", the maximum possible starting index for second subarray is -
	
	"n - (k - 2) - 1"
	
	Because, after second subarray, we have "k-2" subarrays left to create.
	Which means, we need at least "k - 2" elements after the starting index of second subarray.
	
Okay, so we now got the idea about second subarray and its minimum and maximum starting indices.

Now, what about the "dist" value that is given to us?

Since we are given a value "dist" it restricts us to only choose certain indices at a time to be the starting indices of our last subarray. Didn't get it? 

Let's take an example to understand it.

	nums = [1,3,2,6,4,2], k = 3, dist = 3
	
	k = 3 means we need to divide this array into 3 subarrays
	
	Here, dist = 3. 
	
	This means, the difference between starting index of last subarray
	and starting index of second subarray can be at most "3"
	
	For example, if we have a division as - 
	
	[1], [3], [2,6,4,2]
	
	Here, starting index of second subarray is 1
	And starting index of last subarrayt is 2
	And difference is 2 - 1 => 1
	'
	Since 1 <= dist, it means this is a valid divison/
	
	
	Similarly, [1,3], [2], [6,4,2] is also a valid division.
	Because, starting index of second subarray is 2
	and starting index of last subarray is 3, resulting in a difference of 1
	
	Is this division valid - [1], [3,2,6,4], [2] ?
	
	Here, starting index of second subarray is 1
	And starting index of last subarray is  5
	The difference is "4" but "4" is not <= dist.
	
	This means, it is an invalid divison.
	
	So, for this test case, 
	if the starting index of second subarray is "1", 
	we cannot have a starting index of last subarray > "4"
	
	Otherwise, the difference will become > 3 which is invalid.
	
	But, if the starting index of second subarray is "2"
	then we can have starting index of last subarray as "5"
	Because 5 - 2 = 3 and 3 <= dist

So, if we generalize this, we can say that,
	
	If starting index of second subarray is "i"
	Then, the maximum valid starting index of last subarray can be "i + dist"

So, now we are clear with all this. 

Now, we come to the minimum cost sum, something that we have to return in this problem.

For a subarray, its cost is the first element in it. In other words, the element at the starting index. So now you can understand why we focused so much on the starting indices above.

For the first subarray, the first element is always the element at index = 0. So, that's always fixed.

For second subarray, we know that the first element can be any element between indices [1, n - (k - 2) - 1].

And we also know that for any starting index "i" for the second subarray the last subarray will have at most a starting index of "i + dist".

Now, to get the minimum cost sum, we need to make sure that the subarrays after the second subarray (which starts at index "i") have the smallest possible element as their first element.

And since there are "k-2" subarrays after the second subarray, it basically means, those "k-2" subarrays should have smallest possible elements as first elements and the sum of all those will therefore be minimum.

In even simpler words, we want the sum of "k-2" smallest elements in the range [i, i + dist] and once we get that, the overall cost for current divison will be - 

		nums[0] + nums[i] + (sum of k - 2 smallest elements in the range [i, i + dist])
		
And it is not difficult to guess how we are going to find the sum of "k-2" smallest elements in a particular range. Well, we are going to use a MAX HEAP for that.

And that's the whole idea.

# **1. BRUTE FORCE APPROACH - TLE**
In the Brute Force approach, we will take each valid starting index of second subarray "i", and then find the "k-2" smallest elements in the range [i, i + dist].

While this approach is valid, it will give TLE. Why? Because for each starting index, we have to traverse the whole list on right (till the valid index), and get "k-2" smallest elements in that range. So, how can we improve it? For that, we have the second approach.

# **2. TWO HEAPS APPROACH**

If you think about it, there is absolutely no need to recreate the whole heap from scratch for every new starting index of the second subarray.

For example,

	nums = [10,1,2,2,2,1], k = 4, dist = 3
	
	We start with i = 1 for second subarray
	
	This means, we need to get the "k - 2" smallest elements in the range [i + 1, i+dist]
	Since i = 1 and k = 4, we can say

	we need the "2" smallest elements in the range [2, 4]
	
	What are the 2 smallest elements between indices "2" and "4" (both included)
	
	They are "2" and "2". So, the sum of "k-2" smallest elements on right of "i" is 4
	
	And so, if second subarray starts at index "i", the minimum cost sum possible is 
	
	nums[0] + nums[i] + 4 => 10 + 1 + 4 => 15
	
	Now, we increase i. Now, i = 2.
	
	Do we now need to re-check the whole range [i + 1, i + dist] again?
	
	There is absolutely no need for that.
	
	Because, all that happened is that i increased from i to i + 1
	
	And so, the maximum starting index possible for last subarray also increased by 1 
	from "i + dist" to "i + 1 + dist".
	
	All the elements between "i+1" and "i + 1 + dist" remain unchanged.
	
We just have to play around with these two newly added elements.
	
Since "i + 1" was one of the candidates for the "k-2" smallest elements for the previous starting index "i", it is no longer the candidate now, because the starting index now is "i + 1".
	
This means, if it is one of the "k-2" smallest elements that we have so far considered, we need to remove it and in its place, we need to consider some other element.
	
Now, for that some other element, we can maintain a second heap, which will be a MIN HEAP.
	
Why a minHeap? 

Let's understand with the help of an example.

	nums = [10,1,2,2,2,1], k = 4, dist = 3
	
	when i = 1, the range from which we want k - 2 smallest elements is [2,4]
	
	The candidates are [2,2,2]
	
	And two smallest are [2,2] 
	
	Now, it is important to deal with duplicates here.
	
	Since "2" occurs at index 2,3 and 4
	the best two candidates at the moment are the ones at index "2" and "3"
	
	The one at index "4" might be a valid candiate later. So instead of discarding it,
	we will push it in a minHeap which will order items from smallest to largest.
	
	In this way, at any time, if our maxHeap size is not "k-2", 
	we can pick values from top of the minHeap
	
	And that's the reason why when we push to a maxHeap in the code,
	we are pushing a triplet -> (-val, -idx, idx)
	
	Why a triplet? Because in case two indices have same values, 
	we want to keep the one on top that has a higher index. That is,
	the one that appears later.
	
	So that if we have to move items to minHeap, 
	we move those items that appear later.
	
	If you see, in the minHeap as well, we are using a triplet.
	It is something lke -> (val, idx,idx)
	
	This means, in our minHeap the value with a smaller "idx" sits above the value with a larger "idx".
	
	Because when we want to get a value from minHeap to push into maxHeap,
	we want those elements that appear sooner in the range from which we want "k-2" smallest values.
	
	That's how we break ties in heaps in python.
	
So, now that we are clear with how a minHeap will be used in this approach, let's see how we will deal with removal of invalid data from the heaps.


	nums = [10,1,2,2,2,1], k = 4, dist = 3
	
	At i = 1, 
	maxHeap will be like [(2,-3,3) , (2,-2,2)]
	and minHeap will be like [(2,4,4)]
	
	We will also maintain the current sum of "k-2" smallest values.
	At the moment, the smallestSum is 2 +2 => 4
	
	So, total cost => 10 + 1 + 4 => 15
	
	Now, before we move to index "i + 1", we need to check if index "i + 1" is present in maxHeap.
	If yes, then we need to remove it.
	
	But ofcourse since it is a maxHeap,
	we cannot remove it efficiently if it is present in between, instead of the top.
	
	That's why, we will also maintain a "set" that keeps track of the indices currently in the heap.
	
	If "i+1" is in the maxHeap, it must also be in this set. So, we simply remove it from this set.
	
	We will only remove that index from maxHeap when it appears on top of the maxHeap.
	That is, LAZY REMOVAL.
	
	This means, at any time, our maxHeap might have those values as well 
	which we have already discarded from the set.
	
	So, we cannot rely on "len(maxHeap)" to get the actual length of the maxHeap.
	
	The actual length is the number of values in the "set". That is "len(set)"
	
	Similarly, when we have some values in the minHeap, 
	before we get some value from it to push back in the maxHeap,
	we have to remove the ones that are no longer valid (from the top).
	
	All those values that have index <= "i" will not be valid anymore so we will remove them.
	
And that's the whole approach using two heaps + a set.
