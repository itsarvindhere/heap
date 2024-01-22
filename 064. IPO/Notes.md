# PROBLEM STATEMENT

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

# EXAMPLE

    Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
    Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

# **1. BRUTE FORCE APPROACH - TLE**
The Brute Force approach is ofcourse not going to get accepted but the advantage is that if you can write a Brute Force solution, then that solution can help you in writing a better solution.

So, we are asked to pick at most "k" projects and we can only pick a project if we have enough capital required. That is, if "w" >= capital[i], where "i" is the index of the project.

Since we want to "Maximize" our profit, it means that at any time, from all the available project, we must pick the one that gives us the maximum profit and we have enough capital to take up that project.

And so, from all the available projects, we will pick the one such project, and update our capital "w" with the profit that we get from finishing this project. And we will also use a Set to keep track of all the finished projects so that we avoid taking up the same project again and again.

If there is no project available to take up with the amount of capital we have, then we can straight away return the maximized capital.

# **2. USING TWO HEAPS**

So, we see that while the above solution is a valid solution, it does not work for large test cases due to time constraints. Hence, we get TLE.

The reason is the inner for loop because we have to traverse this whole list of projects each time we have to pick the most suitable project. And that is a very inefficient way.

The basic idea is that at any time, we want to get the project that gives us the maximum profit and also, its capital doesn't exceed "w". So, one thing we can do is we can use a "MAX HEAP" and put such projects in it so that at any time, the top of the maxHeap has the project that gives us the maximum profit.

But what about other projects that we cannot take up at any time? We might be able to take them up when we have got enough capital, right?

	Let's say we have three projects where,
	
	The first project requires 0 capital and gives us profit of 2 
	The second project requires 1 capital and gives us a profit of 2
	The third project requires 2 capital and gives us a profit of 3

	Initially, let's say we start with w = 0 and k = 2. That is, we can pick at most two projects.
	
	Since w = 0, it means, that initially, we can only take up the first project because its capital value is 0
	That is, its capital value is <= w
	
	Once we finish this project, we now have w = 2 since we get profit = 2 from first project.
	
	So now, we see that we can take up the other two projects as well. How did we know that?
	Because for the second project, the capital required if 1 and 1 <= 2
	Similarly, for third project, the capital required is 2 and 2 <= 2
	
	But, out of these two which one to pick?
	
	Well, if you think about it, it makes sense to pick the project which gives us a profit of 3
	Because we are getting more profit by picking it.
	
But now the question is, at any time, how can we check if, among all the projects we couldn't take previously, are there any projects that we can now take up, now that we have more capital?

If those projects were ordered by their capital value from smallest to largest, then we could easily compare their capital values with "w" and move them back to the Max Heap, from which we can easily pick the project that gives us the maximum profit.
	
And well, for this reason, we can use a second heap which will be a "MIN HEAP" because this will be used to keep those projects that cannot be taken at any time because of low capital. But since it is a "MIN HEAP", we will use it to order those projects by their capital value from the smallest to the largest.

This way, at any time, we can check from the top of this minHeap whether some projects can now be taken up. In that case, we will move them back to the maxHeap. And once a project is in the Max heap, it will always be available to pick up because "w" will always increase, not decrease.

And that's the whole logic of using Two Heaps.