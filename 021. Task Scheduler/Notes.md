# PROBLEM STATMENT

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

# EXAMPLE

    Input: tasks = ["A","A","A","B","B","B"], n = 2
    Output: 8\

Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

# APPROACH

This is quite a tricky problem so I had to refer to this youtube video for the approach - https://www.youtube.com/watch?v=s8p8ukTyA2I

Basically, the most optimal way to execute the tasks will be to execute the most frequent tasks first. So, we will use a maxHeap that gives us the task with the most frequency at any time.

But, once we execute that task, we cannot execute that task again until we are at the "currentTime + cooldownTime" time. So, till the task is not usable, we will put that task into a queue. 

And only when we see that the task is not usable, we will take it out from the queue and put it back in the maxHeap which will order it automatically.

Since there are only uppercase alphabets in the input list, the time complexity of the heap for push and pop will be O(Log26) or a constant time.

Hence, the overall time complexity will be O(N)