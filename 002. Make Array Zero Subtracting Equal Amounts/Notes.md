# PROBLEM STATEMENT

You are given a non-negative integer array nums. In one operation, you must:

 - Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
 - Subtract x from every positive element in nums.

Return the minimum number of operations to make every element in nums equal to 0.

# EXAMPLE

    Input: nums = [1,5,0,3,5]
    Output: 3

Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

# **1. BRUTE FORCE APPROACH**

In the Brute Force approach, we loop over the input list again and again till all elements are not 0.

And in each iteration, we will take the smallest element in the list and then subtract each element of list with that smallest element.

In this problem, this solution gets accepted since the length of input list can be at most 100. But, this is definitely not a good solution at all.

# **2. MIN HEAP APPROACH**

See, at any time, we want to get the minimum element right? So, what is a data structure that can give us the minimum element at any time even after we add or remove some elements from it?  In simple words, we want a data structure that can automatically reorder the elements after removal or addition of a new element.

Well, that data structure is a heap. In this problem, we want the minimum element in the list at any time so we want a "MIN HEAP" here.

But, how are we going to use a heap here? 

See, for that we have to take an example to see exactly what happens when we subtract an element from all elements.

	Let's say, nums = [1,5,0,3,5]
	
	First, we pick 1, so,  [1,5,0,3,5] becomes [0,4,0,2,4]
	Then, we pick 2, so, [0,4,0,2,4] becomes [0,2,0,0,2]
	Finally, we pick 2, so [0,2,0,0,2] becomes [0,0,0,0,0]
	
	Hence, 3 operations were required.
	
	Now, think about it. Let's say we don't manually loop over the list again and again.
	
	And we already know that 3 operations will be required.
	
	And after 3rd operation all elements became 0
	
	So it means, if we sum all the minimum elements in all 3 operations, 
	then that sum should be at least equal to the greatest element in original list.
	
	Because only then the greatest element can be reduced to 0.
	
	In operation 1, the minimum was 1
	In operation 2, the minimum was 2
	In operation 3, the minimum was 2

	So, sum of minimums was 5
	
It means, by the end of 3rd operation, all elements less than or equal to 5 would've been reduced to 0
	
And since in the input list all element are <= 5, the whole list got reduced to only 0s after 3rd operation
	
And if this sum of minimums rule works in the final operation, it should also work for individual operations.
	
	It means,
	
	Since after operation 1, the sum of (current minimum + all previous minimums) is 1
	
	All elements <= 1 (IN THE ORIGINAL LIST) will be reduced to 0 by the end of operation 1
	
	Then, after operation 2, the sum of (current minimum + all previous minimums) is (2+ 1) => 3
	
	All elements <= 3 (IN THE ORIGINAL LIST) will be reduced to 0 by the end of operation 2
	
	And finally, after operation 3, the sum of (current minimum + all previous minimums) is (2+ 3) => 5
	
	All elements <= 5 (IN THE ORIGINAL LIST) will be reduced to 0 by the end of operation 3
	
	
And so, the important thing to understand is this "SUM OF MINIMUMS" and how can we use this sum of minimums now to our advantage.

We will use a heap so that at any time, after we are done removing elements <= sum of minimum so far, we can immediately get the next minimum element for the next operation (by first reducing it be the "sum of minimums")

# **3. OPTIMAL APPROACH**

It is given that the length of the input list won't exceed 100 and will have elements in the range from 0 to 100 only.

So, instead of using a heap, we can use a list of fixed length (101) to keep track of elements and their frequency.

An index in this list will represent an element in the "nums" list.

	For example, if we have nums = [1,5,0,3,5]
	
	Then, the freq list will be something like [1,1,0,1,0,2,0,0,0,0,0....................
	
	At index 0, we have 1 which means "0" occurs once in "nums"
	At index 1 we have 1. which means "1" occurs once in "nums"
	and so on...
	
	And since this list is now sorted by indices, it is quite easy to get the minimum element at any time.
	
	For example, initially, the smallest element is obviously 0 and sum of minimums is also 0
	
	Since we want to skip the 0s, we can start our loop from index/element 1.
	
	At index 1, we have a value > 0 which means this element exists in the "nums" list.
	It the value was 0, we would've skipped this element and moved on to next index.
	
	Now that at index 1, the value is > 0, this is now the current minimum element.
	But, do note that if w did some operations before, we would need to reduce 
	this minimum element by sumOfMinimums so far, just how we did in the heap approach.
	
	And now, we will get the value which would be the smallest value at this particular operation in the list.
	
	And now, we can add this value to our sum of minimums so far, 
	and then all elements in the original list which are <= sum of minimums will be reduced to 0 at this operation.
	
	Finally, we are done with current operation so we increment operation count
	
This solution has a linear time complexity (O(N)) and hence, it is the faster than the two solutions above.