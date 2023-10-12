# PROBLEM STATEMENT

You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

 - If the CPU is idle and there are no available tasks to process, the CPU remains idle.
 - If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
 - Once a task is started, the CPU will process the entire task without stopping.
 - The CPU can finish a task then start a new one instantly.


Return the order in which the CPU will process the tasks.

# EXAMPLE

    Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
    Output: [0,2,3,1]

Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

# APPROACH

See, one thing that's easy to understand is that we will somehow need to keep track of all the available tasks at any time and also, what task has the least processing time out of those available tasks. That is something a minHeap can manage for us. So, that's one thing.

	Let's say we have two tasks as [[2,4], [1,3]]

Now, it is pretty obvious that CPU will start processing at time "1" because that's the smallest enqueue time in the input list. In other words, it will start processing the task [1,3] first. Also, since no other task is available at time "1" (since multiple tasks can have same enqueue time), it will only pick [1,3]. So, we did not have to care about the processing time in this case.

	but, if the tasks list was like [[2,4], [1,3], [1,2], [1,5]]

Then, in this case, we have three tasks available to process at time "1". So, we have to now choose the one that has the least processing time, that is, the task [1,2].

So, at time = 1, CPU starts processing task [1,2] and available tasks are [[1,3], [1,5]]
Since the task [1,2] has processing time of "2", it means it will keep processing this task till time = 3. And only at time = 3, it will be free to choose another task from the available tasks. 

	But at time = 3, we see that the task [2,4] is also available to process now since its enqueue time is <= 3
	so it is also added to available tasks. 

	Available Tasks = [[1,3], [1,5], [2,4]]
	
And so now, the CPU will choose the task [1,3] since it is the one with least processing time.

And this task will take 3 units of time to process. 

And so on.....

So, that's the main idea of the solution below.

Note that when we push some data to the available tasks minHeap, we want to also make sure we handle the cases where two tasks have same processing time. In that case, we want to give priority to the task with a smaller index. That's why, In the code, I am pushing a "triplet" to the availableTasks minHeap where the second value is the original index which will act as a tie breaker as well in case processing time is same for two heaps.
 