# PROBLEM STATEMENT

You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

# EXAMPLE

    Input: nums = [18,43,36,13,7]
    Output: 54

Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

# **1. BRUTE FORCE APPROACH - TLE**
In the Brute Force approach, for every number, we will go over the whole list to find numbers with the same digit sum and then see which one gives the maximum sum. And update the overall maximum value accordingly.

But this solution will give TLE for large test cases.

# **2. DICTIONARY + MINHEAP SOLUTION**
Since all we want are the two largest numbers with the same digit sum, what we can do is, we can create groups such that each group has all those numbers that have the same sum of digits.

	For example, if we have nums = [18,43,36,13,7]
	
	Since 18 and 36 have the same digit sum = 9
	They will be in the same group
	
	Similarly, 7 and 43 will be together in a different group
	
In this way, once we group the numbers, then we can easily get the two largest numbers in each group and get their sum and update the overall maximum value accordingly.

Now, since we want only the two largest numbers of each group, there is no need to keep more than two numbers in every group. We just keep the two greatest numbers and we do that using a minHeap. So, each group is a minHeap of size 2 which keeps at most two largest numbers.

# **3. DICTIONARY + SIMPLE LIST SOLUTION**
Finally, we come to the most optimal approach. 

Since all we want are the two greatest numbers in each group, a minHeap is an overkill for this simple task. We can easily keep track of which is the greatest and secondgreatest in each group and update them accordingly if a new number has to be pushed into this group.

We will use a simple list and it will have at most two values only - The first greatest and second greatest.

As we find a number that belongs to a group, we can only push it if - 

	1. Either the group is empty
	2. The group has only one value
	3. Group has two values but either the number is greater than first or greater than second

And well, these simple checks eliminate the need to use a minHeap.