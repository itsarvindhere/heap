# PROBLEM STATEMENT

You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of its engineers' speeds multiplied by the minimum efficiency among its engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 10^9 + 7.

# EXAMPLE

    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2

    Output: 60

Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

# APPROACH

This is exactly the same idea as for **[2542. Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/)**

Here is my solution for that problem - https://leetcode.com/problems/maximum-subsequence-score/discuss/4004474/Python-Sorting-%2B-MinHeap-Approach

There will be just one small change and that's something you can easily figure out. But the main logic remains exactly the same.

# **1. SORTING & MIN HEAP - TLE**

Yes, this solution gave TLE and I was expecting this to happen. Still, this solution was passing 54/55 test cases so it helped me in writing a better solution.

The idea is very simple once you understand it.

See, we want to find the Maximum Performance if we choose at most "k" engineers. And the Maximum Performance is given by - 

	(Sum of speeds of k engineers) * (Minimum efficiency among k engineers)

It is important to note here that we want to choose "AT MOST k" engineers, not "EXACTLY k". This means, we can even choose just one engineer and it is possible that we get a maximum performance from choosing that single engineer as well.

So, the idea is that we can Sort the list of efficiencies in increasing order. 

How is that going to help us?

Let's take an example.

	Suppose, n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
	
	Let's say we sort efficiency in increasing order - 
	
		efficiency = [2,3,4,5,7,9]
		
	And speed will hence become - 
		
		speed = [8,3,10,2,5,1]
		
	Now, let's say we start with the first engineer that has efficiency = "2" and speed = "8"
	
	We already have one engineer so we can select at most "k-1" more engineers in this group.
	
	We will only select those engineers from the right side of the current engineer.
	
	And the benefit is that, since the efficiency list is sorted, among all the "k" engineers we get at the end,
	the minimum efficiency will always be the one that the first engineer has.
	
So, since we already know that minimum efficiency is always going to be the same as for the very first engineer we pick for a group, the only thing we need to now care about is the sum of speeds, which we want to be the maximum.
	
So, we want the "k-1" largest speed values since they will give us the maximum sum.

	Since we already selected one enginer with speed = "8"
	
	We can now select the other "k-1" speeds from these only -> [3,10,2,5,1]
	
	Since k = 3, it means we can pick at most "2" more engineers in this group.
	
	And so, we need the "k" largest speed values from [3,10,2,5,1]
	
	Those are "10" and "5".
	
	And so, the sum of speed becomes (8 + 10 + 5)
	And the minimum efficiency, as we know, is "2"
	
	Hence, performance = 23 * 2 => 46
	
And in this way, we will go over each index, pick that engineer as the first engineer, and then try to find the rest of the "k-1" engineers if we can. It doesn't matter if we don't find exactly "k -1" other engineers since the problem mentioned "AT MOST k".
	
While this solution doesn't look that bad, it will fail for large test cases because for each index, we have to traverse over the entire list on the right side just to find the top "k  - 1" speed values. This is not efficient.


# **2. SORTING & MIN HEAP - ACCEPTED**

Instead of sorting the "efficiency" list in increasing order, a better way is to sort it in decreasing order.

Suppose, n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
	
	Let's say we sort efficiency in decreasing order - 
	
		efficiency = [9,7,5,4,3,2]
		
	And speed will hence become - 
		
		speed = [1,5,2,10,3,8]
		
	So now, since efficiency if sorted in decreasing order, it we pick any engineer "i" from this list, 
	we know that this is the minimum efficiency among all the efficiency values on the left side.
	
	And since we already know this, 
	all that we require are the top k speed values so far (including current engineer's speed value)
	
	For that, we can use a min heap.
	
Now, by simply switching the order in which we sort the efficiency list, we can write a much efficient solution. Because now, for every new index, we do not have to iterate over the entire list to find top k - 1 speed values. Because, for any new index "i", we just need top k speed values on its left (including itself). And since we are using a min Heap, it will always have the top k values so far. 

Continuing with the example, 

	efficiency = [9,7,5,4,3,2]
	speed = [1,5,2,10,3,8]
	k = 3
	
	We can first have the top "k" speed values in the minHeap initially.
	
	Since k = 3, we will iterate over the first three indices and put the speed values in the minHeap.
	The minHeap will automatically order them such that the value on top is smallest and the one on the bottom is the largest.
	
	Along with this, we will also keep calculating the sum of "k" highest speed values.
	
	And along with that, we will keep updating the maximum performance value. 
	Because remember that we can also pick less than k employees and that might also give us a maximum performance.
	
	So, we start with i = 0 and max performance = 0
	Speed is "1" and efficiency is "9".
	
	Sum of "k" highest speeds = 1
	
	So, performance = 1 * 9 => 9
	
	We update the maximum performance
	
	Next, i = 1.
	Speed is "5" and efficiency is "7"
	
	Sum of "k" highest speeds = 1 + 5 => 6
	
	Note that now, the minimum efficiency is "7" because remenber that the list is sorted.
	
	So, performance = 6 * 7 => 42
	We update the maximum performance.
	
	Next, i = 2.
	Speed is "2" and efficiency is "5"
	
	Sum of "k" highest speeds = 1 + 5 + 2 => 8
	Minimum efficiency = 5
	
	So, performance = 8 * 5 => 40
	Maximum performance is not updated since 40 < 42
	
And after this first loop, we have traversed the first "k" engineers and found that from them, the maximum performance value that we can achieve is "42".

Now, we will go over the rest of the engineers, starting with the index "k" till the index "n - 1".

We can do this all in a single loop with if else statements but I did it this way just so that you can see that this solution is exactly the same as my solution for **[2542. Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/)**

	
	efficiency = [9,7,5,4,3,2]
	speed = [1,5,2,10,3,8]
	
	
	Now, we are at index i = 3
	MinHeap so far is [1,2,5]
	And Maximum Performance so far is 42
	Sum of "k" highest speeds so far is 8
	
	At index i = 3, we have speed = 10 and efficiency = 4
	So, we push this value to the minHeap
	Min Heap becomes [1,2,5,10]
	Sum of "k" highest speeds so far becomes 8 + 10 => 18
	
	We always want the Min Heap to have at most "k" values.
	But since we now have one extra value,
	we will remove the smallest speed value from top of the Min Heap.
	
	Since we remove "1", this will also be subtracted from the Sum of Speeds.
	Sum of "k" highest speeds becomes 18 - 1 => 17
	
	So, you can see that now, we are making sure that MinHeap always has at most "k" values in it
	And similarly, the Sum of "k" highest speeds always have the correct sum value.
	
	And finally, all that's left is to update the maximum performance.
	
	With current engineer picked, the performance becomes 17 * 4 => 68
	
	Since it is higher than the maximum performance, we update the maximum performance to 68.
	
And this is something we will keep doing till we reach the end of the list.
	
And finally, we will have the Maximum Performance value that we have to return.