# PROBLEM STATEMENT

There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

  For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.

When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

# EXAMPLE

    Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
    Output: 1

Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
  
Since friend 1 sat on chair 1, we return 1.

# APPROACH

I felt this problem is quite similar to the "Single-Threaded CPU" problem - https://leetcode.com/problems/single-threaded-cpu/

At least some part of it felt similar while I was writing the solution.

In that problem too, we had a minHeap which was used to keep track of the "tasks" that CPU could choose to process and at any time, the CPU was taking task to process based on its processing time from smallest to largest. And in each iteration, we were checking if there were tasks already finished executing by the time the current task was added.

And the similar approach is used in this problem as well. We are asked to assign chairs such that the friend gets the chair with the lowest number. And so, we have a minHeap here to keep track of all the availableChairs that a person can take. And it is a minHeap because at any time, we want the chair with the lowest number.

Also, in each iteration, we check whether there are friends who "leave" at or before the time when the current friend "arrives". In that case, those chairs will be available too.

And the rest, I think, is pretty easy to understand.