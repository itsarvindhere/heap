# PROBLEM STATEMENT

You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

 - The first n elements belonging to the first part and their sum is sumfirst.
 - The next n elements belonging to the second part and their sum is sumsecond.
  
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

 - For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
 - Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
  
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

# EXAMPLE

    Input: nums = [7,9,5,8,1,3]
    Output: 1

Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.

# APPROACH

First, let's start with the idea of the solution.

See, we are given a list of "3n" integers and from this list, we have to remove "EXACTLY" n integers. This means, we will be left with "2n" integers after removal. And then, we have to divide that result list into two parts, each having "n" elements each. 

And so, we are asked to return the minimum difference between these two parts.

So, if I ask you that if I have "X" and "Y", and I want to minimize the difference "X-Y", what can we do? The simplest solution is to increase the value of "X" and reduce the value of "Y" as much as we can. In this way, we will achieve the minimum possible difference.

And that's exactly what we do to minimize the difference between the two parts in this problem.

	The Sum of First part needs to be minimized, 
	and the Sum of Second Part needs to be maximized. 
	
Let's take an example.

	nums = [7,9,5,8,1,3]
	
	The most optimal solution here is to remove "9" and "1" 
	to get [7,5] and [8,3] as the two parts
	
	Instead of deciding which elements to remove, what if we focus on the sum of these two parts instead?
	
	We know that the first part needs to have as minimum sum as possible. 
	
	And in this example, n = 2 so each part needs to have "2" elements.
	
	Now, where all we can partition so that we have at least "2" elements on left and right 
	so that we can pick the most optimal ones?
	
	We can definitely not partition at index 0 because if we do that, we will have [7] and [9,5,8,1,3]
	
	But, we need at least "n" numbers if we want to choose the most optimal "n" numbers.
	
	This means, index 0 is not a valid index for partitioning.
	
	Similarly, we cannot partition at the last index because if we do that, we have [7,9,5,8,1] and [3]
	
	Again, we need at least "n" values.
	
So, now that we have this all cleared out, now, let's see for the "first part" in the resultant array where all we can partition.
	
	FOR FIRST PART -
	
	Partition at index 0 -> [7] and [9,5,8,1,3] => NOT VALID
	Partition at index 1 -> [7,9] and [5,8,1,3] => VALID
	Partition at index 2 -> [7,9,5] and [8,1,3] => VALID
	Partition at index 3 -> [7,9,5,8] and [1,3] => VALID
	Partition at index 4 -> [7,9,5,8,1] and [3] => NOT VALID
	Partition at index 5 -> [7,9,5,8,1,3] and [] => NOT VALID
	
	So, as we can see, for the first part, the only valid partition indices are 1, 2 and 3
	
	In other words, all the indices from "n - 1" to "2n - 1"
	
Similarly, let's see for the second part, what all are the valid parition indices.
	
	FOR SECOND PART - 
	
	Partition at index 5 -> [7,9,5,8,1] and [3] => NOT VALID
	Partition at index 4 -> [7,9,5,8] and [1,3] => VALID
	Partition at index 3 -> [7,9,5] and [8,1,3] => VALID
	Partition at index 2 -> [7,9] and [5,8,1,3] => VALID
	Partition at index 1 -> [7] and [9,5,8,1,3] => NOT VALID
	Partition at index 0 -> [] and [7,9,5,8,1,3] => NOT VALID
	
	So, for the second part, the only valid partition indices are 4, 3, and 2
	
	In other words, from "2n" to "n"
	
Now, from all the valid partitions for the First part, we need to find the minimum sum possible. And to get the minimum sum possible, we need the "n" smallest elements. And the most efficient way to get "n" smallest elements from some list is using a "MAX HEAP". And that's what we are going to use here.

Because, if you try to take each valid partition for the first part, take its elements, sort them, and then find the k smallest ones, then get the sum, that will not be a good approach.

If we have a Max Heap, all we need to do is to maintain the length of the Max Heap as "n" and at any time, the Max Heap will always have the "n" smallest elements in it.

	nums = [7,9,5,8,1,3]
	
	We know that a valid partition index for the first part is between "n - 1" to "2n - 1",
	That is, from index 1 to 3
	
	So, until we don't reach the index "n - 1", we don't start doing anything, except for putting the elements in the Max Heap 
	and also adding them to the running sum of the first part.
	
	Here, n = 2. 
	
	So the valid partition index starts from index 1. 
	
	When we are at index 0 initially, we will simply push the first element in the max heap and add it to the sum as well.
	
	So, at index = 0, max Heap is [7] and sum = 7
	
	At index = 1, we now are at an index that is a valid index for partition.
	
	So, we put the value in the max heap and it becomes [9,7]. The sum becomes 7 + 9 => 16
	
	Now that we are at an index that is a valid partition index,
	we can now find the minimum sum possible for the first part if we partition at this point.
	
	Since we are already calculating the running sum, it is "16" for this index.
	
	Let's create a new array "leftSum" just to keep this data.
	
	Initially, leftSum has all zeros.
	
	So, leftSum will be like [0,16,0,0,0,0] at this point.
	
	At index = 2, we have element "5" so we put it in the max heap.
	
	Max heap now becomes [9,7,5] and sum is 16 + 5 => 21
	
	And now remember that we want the maxHeap size to be maintained as "n".
	
	Since it now exceeds n = 2, we need to pop the top element. So, we remove "9".
	
	Since we removed 9 from the heap, it also needs to be reduced from the sum. So, sum = 21 - 9 => 12
	
	And so, this is the advantage of using a maxHeap. 
	
	At index = 2, we were quickly able to find that till the index "2" (including itself),
	the minimum possible sum of "n" elements is 12
	
	And so, leftSum now becomes [0,16,12,0,0,0]
	
	At index = 3, we have element = "8"
	
	So, maxHeap becomes [8,7,5] and sum becomes 12 + 8 => 20
	
	But again, the size of maxHeap exceeds "2" so we pop 8 and reduce the sum by 8 as well.
	
	Max Heap = [7,5] and sum = 12
	
	So, leftSum becomes [0,16,12,12,0,0]
	
We cannot move any further because for the first part, the valid partition indices are from 1 to 3. So, that's our first part done.

Now, we will do the same thing for the second part by going over all its valid partition indices are get the maximum sum of n elements on the right side of a partition index (including itself). As we want the "MAXIMUM" sum of "n" elements, we will use a "MIN HEAP" here and maintain its size as "n".

As we want the "MAXIMUM" sum of "n" elements on the right of each partition index, we will start the loop in reverse for the second part. That is, from right to left.


	nums = [7,9,5,8,1,3]
	
	Valid partition indices are between 2n and n. That is, between index "4" and "2", both included.
	
	So, we start with the last index. That is, index = 5
	
	This is not a valid partition index. So, we simply push it to minHeap and also add it to sum.
	
	MinHeap = [5] and sum = 5
	
	At index = 4, we have "1".
	
	MinHeap = [4,5] and sum = 9
	
	Also, since "4" is a valid partition index, we can now take this sum and put it in a "rightSum" list.
	
	rightSum = [0,0,0,0,9,0]
	
	At index = 3, we have "8".
	
	MinHeap = [4,5,8] and sum = 17
	
	Here, size of MinHeap exceeds "n" so we have to remove the top element at this point.
	
	We remove "4" and also reduce the sum by 4. 
	
	So, MinHeap = [5,8] and sum = 13
	
	And rightSum = [0,0,0,13,9,0]
	
	At index = 2, we have "5"
	
	MinHeap = [5,5,8] and sum = 18
	
	Again, the heap size exceeds "n" so we remove "5" from the top and reduce the sum by "5".
	
	So, MinHeap = [5,8] and sum = 13
	
	And rightSum = [0,0,13,13,9,0]
	
	And we stop.
	
So, we now have two lists with us - "leftSum" and "rightSum".

	A value leftSum[i] will give us the minimum sum of "n" elements on the left side of "i" index (including itself)
	A value rightSum[i] will give us the maximum sum of "n" elements on the right side of "i" index (including itself)
	
So now, we can find the Minimum Difference.

We can go over every valid partition array for one part, and use both these lists to find the difference and then update the maximum difference accordingly.

	As we know, for the first part, valid partition indices are from n - 1 to 2n - 1
	
	nums = [7,9,5,8,1,3]
	leftSum =    [0,16,12,12,0,0]
	rightSum = [0,0,13,13,9,0
	
	So, we go over these indices.
	
	Here, n = 2 so, the loop runs from indices 1 to 3
	
	At index 1, we assume that we divided the input list into two parts [7,9] and [5,8,1,3]
	
	And so, we want the minimum sum of "n" elements from [7,9] and maximum sum of "n" elements from [5,8,1,3]
	
	And now, we can use our leftSum and rightSum lists.
	
	So, what is the minimum sum of "n" elements on left of index "1" (including itself)?
	
	Well, that is simply leftSum[1]
	
	And what is the maximum sum of "n" elements on right of index "2" (including itself)
	
	Well, that is leftSum[2]
	
	So it means, if we partition at index 1, the minimum difference possible is leftSum[1] - leftSum[2]
	
	That is, 16 - 13 => 3
	
	And it makes sense because if we partition at index 1, the most optimal two parts that we will get will be - 
	
	[7,9] and [5,8]
	
	And similarly, we will now go over each index between n - 1 and 2n - 1, 
	get this minimum difference, and then update the overall minimum difference.
	
	
And finally, we get the overall minimum difference which we have to return.