# PROBLEM STATEMENT

You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

 - Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
 - Add the value of the chosen integer to score.
 - Mark the chosen element and its two adjacent elements if they exist.
 - Repeat until all the array elements are marked.

Return the score you get after applying the above algorithm.

# EXAMPLE

    Input: nums = [2,1,3,4,5,2]
    Output: 7

Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.

# **1. BRUTE FORCE SOLUTION - O(N^2)**

As the problem statement says, we repeat the steps until we have marked all the elements in the list.

So basically, until the number of marked elements are not "n", we have to get the current smallest unmarked element, increment the score, and mark its left and right elements, if possible.

In the Brute Force approach, in each iteration, we will have to traverse the whole list to get the smallest at that point hence, the overall time complexity becomes O(N^2) and so, this solution fails for large test cases.

# **2. SORTING SOLUTION - O(NLogN)**
From the Brute Force solution, it is easy to figure out that the reason why it fails is because we have to find the next smallest element in each iteration. But, what if we knew what index would be the smallest at any point of time? We can know that by sorting the list.

But do note that since the marking of indices has to be done on the original list, we cannot sort the original list. We have to create a whole new list that has a pair at each index - (element, original index). And then, we can sort the list by the elements in increasing order.

In this way, we can know at any time, what index in the original list will have the smallest element.

	For example, nums = [2,1,3,4,5,2]
	
	So, first we create pairs -
	
	newList = [(2,0), (1,1), (3,2), (4,3), (5,4), (2,5)]
	
	And now, we can sort it in increasing order
	
	newList = [(1,1), (2,0), (2,5), (3,2), (4,3), (5,4)]
	
	So now, in each iteration we can easily get the smallest index in original list
	by keeping track of the newList indices.
	
	So initially, newList[0] is the smallest -> (1,1)
	It means, in the original list, the index "1" will have the smallest element in first iteration
	
	So, we will increment score by 1. Score = 1
	And mark the elements on left and right.
	
	So, we mark the indices 0 and 2, and also itself.
	
	Marked Indices = [0,1,2]
	socre = 1
	
	Next, we see newList has next smallest index as 0. But, it is already marked.
	Next, we have the smallest index as "5". At "5", we have element 2
	
	So, score += 2 => 3
	And we mark the elements on its left and right (if they are present)
	marked indices = [0,1,2,4,5]
	
	Next, the smallest index is "2" but it is already marked
	Next, the smallest index is "3" so, again, we increment score by nums[3] => 4
	
	Score += 4 => 7
	And finally, we have marked all the indices = [0,1,2,3,4,5]
	
	And our loop ends
	
So, the final score is 7.

And that's the whole idea of Sorting approach.

# **3. MINHEAP SOLUTION - O(NLogN)**

We can also use a MinHeap to get the smallest element and its original index from the top of the minHeap at any time. The solution is almost similar to the Sorting solution, just that we don't have to explicitly keep track of the smallest element's index since we know smallest in a minHeap is always the top element.