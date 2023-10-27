# PROBLEM STATEMENT

You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.

# EXAMPLE

    Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
    Output: [2,2,0,2,1,2]

Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

# APPROACH

    We have some "servers" and some "tasks".
	And each task "i" takes "tasks[i]" seconds to process. 
	This means, if a server starts processing a task, 
	then it will remain busy for "time at which it picked the task + tasks[i]" seconds.
	
	Also, if we have no servers available, we have to wait till at least one server gets free.
	And when it gets free, at that "time", there can be multiple tasks that are available to process.
	
	And in that case, we can process multiple tasks at that time if we have multiple available servers.
	
	And that's one thing the problem statement doesn't clearly explain as the wording is quite poor.
	
So, keeping all this in mind, let's now talk about the solution.

Since we want to pick the "servers" on the basis of their weights, we can use a minHeap here so that at any time, we can get the server with the smallest weight. Since two or more servers can have the same weight, we can use their indices to order them in case of a tie. For that, in Python, we can pass a triplet to the minHeap so that in case of a tie, the heap orders the elements by the second value in the triplet.

We also need to keep track of the servers that are currently processing tasks. So, we need to order them by the time at which they will become free so that we can quickly check what all servers are already free and put them back in the free servers minHeap. And so, another minHeap is required here for "busyServers".

Finally, we need to keep track of the "time" at which a "server" can pick a task.

If there are no free servers, then a task can be picked by the server that finishes executing the earliest among "busyServers". So, in that case, we can update our "time".

In some edge cases, the "time" can be smaller than the current index "i" which should happen because "time" should always remain >= i. So, we always want the greater value among "time" and "i".
