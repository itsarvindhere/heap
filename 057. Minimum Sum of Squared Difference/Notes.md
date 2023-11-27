# PROBLEM STATEMENT

You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

# EXAMPLE

    Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
    Output: 43

Explanation: One way to obtain the minimum sum of square difference is: 
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be: 
(2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

# APPROACH

Before we start writing the solution, it is important to analyze a few examples and to understand how we will select for what index we should apply an operation.

So, Let's take an example

	 nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
	 
	 So, if we take each index and get the square of the difference of the numbers
	 We will get something like this for each index- 
	 
	 [16,16,16,9]
	 
	 So, sum of squared difference will bne 16 + 16 + 16 + 9 => 57
	 
Now, for each test case, we are also given two values "k1" and "k2".

"k1" means that we can take any number at an yindex in nums1, and increment or decrement it by at most "k1" times.
In short, we have "k1" operations to perform on nums1 where each operation is either increment by 1 or decrement by 1.

And the same is the case of "k2" for nums2.

In above example, k1 = 1 and k2 = 1

This means, we can take any index in nums1, and increment or decrement the number at that index by 1.

So, which number should we increment or decrement?

	Let's first try the increment operation on each index of nums1
	and see how it changes the final result
	
	nums1 = [1,4,10,12]
	nums2 = [5,8,6,9]
	
	Increment "1" at index "0", the final output will be [9,16,16,9] => 50
	Increment "4" at index "1", the final output will be [16,9,16,9] => 50
	Increment "10" at index "2", the final output will be [16,16,25,9] => 66
	Increment "12" at index "3", the final output will be [16,16,16,16] => 64
	
	Now, let's try the decrement operation on each index and see how it changes the final result
	
	nums1 = [1,4,10,12]
	nums2 = [5,8,6,9]
	
	Decrement "1" at index "0", the final output will be [25,16,16,9] => 66
	Decrement "4" at index "1", the final output will be [16,25,16,9] => 66
	Decrement "10" at index "2", the final output will be [16,16,9,9] => 50
	Decrement "12" at index "3", the final output will be [16,16,16,4] => 52
	
So, one thing that we can see from the above analysis is that, for all those indices at which nums1[i] is greater than nums2[i], the decrement operation will result in a smaller squared difference for that index. For example, at index "2", we have "10" in nums1 and "6" in nums2. So, if we decrement 10 -> 9 then, the squared difference reduces from 16 to 9. 

And if you think about it, it makes sense, right? The closer the two elements are, the smaller their difference will be. And the smaller their difference is, the smaller the square of difference will be.

It means, for any index "i", the smallest possible squared difference is "0" which means both the elements at that index are the same.

So now that we understand this thing, the question now is, how can we select at which index to apply this increment or decrement operation?

Well, again, if you think about it, the index that contributes the most to the final output should be the one on which we first apply the operation. 

	For example, this is the contribution of each index towards the final output
	if we don't apply any operation - 

		[16,16,16,9]
		
	So, there are three indices that contribute the same to the final result.
	
	So it means, we can select any of these three and apply one operation on that.
	
	This is very important to understand! 
	
	Just because "16" is the largest value does not mean 
	we should apply all the operations on this one index just to make it as close to 0 as possible.
	
	That would not ensure that we get the smallest possible sum of squared difference.
	 
	For example,  nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
	
	Here, we can apply one operation on nums1 and one on nums2.
	
	And since we know that index 0 will contribute "16" to the final result, what if we apply both operations on index 0?
	
	At index 0, nums1 has "1" and nums2 has "5"
	So, we increment nums1 and we decrement nums2
	
	This means, now, at index 0, nums1 has "2" and nums2 has "4", resulting in a squared difference of "4"
	
	So, final sum is 4 + 16 + 16 + 9 => 45
	
	But, is this the smallest?
	
	Now, let's apply just one operation on index 0. 
	Doesn't matter if we increment nums1[0] or decrement nums2[0] or vice versa.
	
	So, let's say we increments nums1[0] so it now becomes 2.
	
	So, we used all of our operations for nums1.

	Now, since index 1 also contributes 16 to the final output, let's apply one operation on nums2
	Since at index 1, nums1 has "4" and nums2 has "8", we should decrement nums2[1] here to get a smaller value
	
	So, now, at index 1, nums1 has "4" and nums2 has "7" and the new squared difference for index 1 is "9"
	
	And so, final output becomes -> 9 + 9  + 16 + 9 => 43!
	
	And that's the smallest possible squared difference we can get!

So, what it means is that, at any time, we want the index that contributes the maximum value to the final output, apply one operation on it, and then move on to the next index that has the next greatest value. And one data structure that can do this for us is a Max Heap. A Max Heap will always have the largest value on top at any time and we can take advantage of it.

# **1. MAX HEAP APPROACH WITHOUT DICTIONARY - TLE**

So, let's try to use a Max Heap.

We will simply get the contribution of each index initially, without using any operations, and put that data in the maxHeap so that each index is ordered by its contribution in the maxHeap.

And then, we can do what we understood above.

That is, while we have operations, we will pick the index with the largest contribution at that time, and then if "k1"  is not yet 0, we can apply an increment or decrement operation on nums1[i]. If k1 is 0, we can apply an increment or decrement operation on nums2[i].

And whatever new squared difference we then get, we will again push it in the maxHeap.

And this process goes on until we no longer have any operations left, or the maxHeap no longer has a non-zero value to reduce because as we know, "0" is the smallest possible difference we can have for any index.

But, the issue with this approach is that, this is not efficient. 

k1 and k2 can be up to 10^9

So, just imagine what will happen in the worst case where in each iteration, we just keep incrementing and decrementing each value by "1" and keep pushing it back in the heap. That will take a lot of time and so, this solution will give us TLE. 


# **2. MAX HEAP APPROACH WITH DICTIONARY - ACCEPTED**

How can we improve the above approach then?

Again, let's go back to our initial example.

	nums1 = [1,4,10,12]
	nums2 = [5,8,6,9]
	
	And output without operations -> [16,16,16,9]
	
Since we have k1 = 1 and k2 = 1, it basically means we have 2 operations in total. Because, we know that for an index, no matter if you increment the value in nums1[i] or decrement the value in nums2[i] or vice versa, the final squared difference is going to be the same. 

Now, "16" exists 3 times in the output if we don't apply any operations.

But since we have "2" operations, it means we can take two of the three "16" values and then reduce them to "9". Makes sense?

And we can do that in one iteration itself, instead of having two different iterations where we first reduce the first "16" to "9" and then the second "16" to "9".

And that's the optimization that we can add to our above approach.

If we keep track of each squared difference and how many times it occurs, then, when we start applying operations, we can do that very efficiently.

That's why, in this optimized approach, we can use a "Dictionary" or "Hashmap" to keep track of each squared difference and its frequency.

And in this way, our maxHeap will have only unique values.

Now, at any time when we get the top value from the maxHeap, we can then instantly check how many indices will give us that same squared difference. And if we have enough operations available we can reduce the squared difference for all those indices at once.

And even if we don't have enough operations, we can still convert at least some of them to a smaller value.

	For example, if we have dictionary such as {16: 3, 9:2}

	And the top value in heap is "16". 
	
	It means, there are three indices that will contribute "16" to the final sum.
	
	And suppose that at this point, we have operations available = 6
	
	Since we have more operations than the count of "16", 
	it means, we can convert all three "16" to "9"
	
	How did we know that "16" will be converted to "9"?
	
	Let's say for index "i", the contribution is 16
	So, when we apply one operation, 
	we will either increment nums1[i] or decrement nums1[i] or increment nums2[i] or decrement nums2[i]
	
	All we want is to reduce the difference between nums1[i] and num2[i] by 1.
	Earlier, the difference was "4" that's why we got "16" as the square.
	
	And when we reduce the difference by 1, then, the difference will be "3" and so, square will be "9"
	
	So, the new difference is simply (squareRoot of 16) + 1
	And so, the new square of difference is simply the square of above value.
	
And the rest is pretty straightforward. 