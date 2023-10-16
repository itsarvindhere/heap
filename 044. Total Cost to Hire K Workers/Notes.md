# PROBLEM STATEMENT

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

 - You will run k sessions and hire exactly one worker in each session.
 - In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
    - For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
    - In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
 - If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
 - A worker can only be chosen once.

Return the total cost to hire exactly k workers.

# EXAMPLE

    Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
    Output: 11

Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.

# APPROACH

This problem may seem tricky at first but after going over the problem statement and the examples a couple of times, it will become very simple to solve.

See, the basic idea is that we want to hire "k" workers and we want the cost of them to be as minimum as possible. There is also a concept of candidates in this problem and that's the thing which makes this problem a bit tricky at first. Because, if there were no candidates concept here, then we could've simply sorted the list or maybe used one minHeap and returned the sum of top "k" lowest costs.

But, here, we have another input given as "candidates".

As the problem statement says, in each iteration, we will choose a worker from either the "first candidates" workers, or the "last candidates" workers.

To understand it better, let's take an example.

	costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
	
	We want to hire 3 workers.
	
	So, there will be "3" hiring sessions.
	
	In first session, we want to get a worker from first "4" and last "4" workers.
	
	And we want this cost to be as low as possible.
	
	First "4" and "Last 4" workers and their costs are [17,12,10,2] and [2,11,20,8]
	
	And we can see that the lowest is "2" and "2" appears in both lists.
	
	But since we want to give priority to the lower index, we will choose the "2" from left part.
	
	So now, left part is [17,12,10] and right part is [2,11,20,8]
	
	We will always try that both lists have  "4" workers. 
	
	And we can do that by adding one worker in a list after we removed one from it.
	
	But we can only add if we have workers available that are not part of any of the two lists.
	
	Here, the only worker that is not part of any of the two lists is at index 4 with cost = 7
	
	And since left list need one extra worker to have "4" workers, we will add it in left list
	
	So now, left = [17,12,10,7] and right = [2,11,20,8]
	
	Again, we do the same. This time, we choose "2" from the right part.
	
	So now, left = [17,12,10,7] and right = [11,20,8]
	
	Since we don't have any worker to add, we move on.
	
	Again, we do the same. This time, we choose "7" from the left part.

	So now, left = [17,12,10] and right = [11,20,8]
	
	And since our "k" sessions are finished, we stop the process.
	
So, the total cost to hire "k" workers in this case will be -> 2 + 2 + 7 => 11

And so, we can understand that here, we will have to keep track of the left and right parts separately. And from each part, we want to quickly check what is the minimum cost available. And that's something we can do using a minHeap. So, we will use Two Min Heaps in this problem.

Also, we will have to keep track of what are the remaining workers that are not part of any of the list yet. So that we can put them in the respective candidate lists when some list has less workers.

There will also be some edge cases where first list has some values whereas other is empty and vice versa. So, we also have to take care of those edge cases while choosing workers.