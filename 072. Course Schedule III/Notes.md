# PROBLEM STATEMENT

There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

# EXAMPLE

    Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    Output: 3

Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

# APPROACH

The idea is pretty simple.

In real-world, if we are asked to do courses, then the best way to approach them would be to first complete those courses that will end first. And that's why, in this problem as well, we will Sort the courses by their deadline day so that we can take those course first which end first.

The next thing is that we also want to complete maximum number of courses out of all.

To understand how we will maximize this count, let's take a simple example with three courses -

	courses = [[10,11], [5,12], [4,13]]
	
	Here, we have sorted the course by their deadline days.
	
	Course 1 takes "10" days to complete and it should be completed by day "11"
	Course 2 takes "5" days to complete and it should be completed by day "12"
	Course 3 takes "4" days to complete and it should be completed by day "13"
	
	So, ideally, we should first do the course [10,11] because its deadline is the earliest.
	So, we take it and this means, we finish it on day = 10
	
	Now, on day 11, we can take course [5,12] but if we do that, the day on which it will be finished is "15"
	And it means it exceeds the deadline. 
	
	Can we take the course [4,13]? Even that is not possible because it will be done on day 10 + 4 => 14
	But the deadline is 13.
	
	So does that mean we can only complete 1 course? NO!
	
	See, the reason why we couldn't do [5,12] or [4,13] after we did the course [10,11] is because
	the course [10,11] alone takes our 10 days. 
	
	But instead of this, if we had taken [5,12] first, then it would've taken only "5" days to complete.
	
	And then, we could've picked the course [4,13] which we would complete on day 9.
	
	So, if we take the course [10,11], then we can only finish one course.
	
	But if we take the course [5,12] then we can also finish the course [4,13]
	
And so, the idea is that, if you have taken 1 or more courses so far, and have spend "x" number of days already, then for the current course, there are two scenarios - 

	1. You can take it because "x" + current course's duration is <= current course's deadline. Then, its fine.
	2. You cannot take it because "x" + current course's duration is > current course's deadline. Then that's an issue

So, if we cannot take current course, just because we don't have enough days left to do it before deadline, why cannot we undo a course that we have already taken, and instead do the current course, only if after undoing, we can finish the current course in less number of days than what it took for the course that we are undoing. Sounds confusing? Let me explain.

	So, when we reached the course [5,12], we had already taken the course [10,12]
	
	And so, the days spent so far were 10
	
	We couldn't take the course [5,12] since 10 + 5 is > 12
	
	But, if we had not taken the course [10,12] then the number of days spent would be 10 - 10 => 0
	
	And so, if we had taken the current course in its place, then number of days spent will be 0 + 5 => 5
	
	And in both the cases, we complete one course, so the overall count of courses taken so far does not decrease as well.
	
	But since taking the course [5,12] is increasing the number of days by a smaller value than [10,12]
	it means, if we take [5,12] then we have more chances to complete the upcoming courses
	because we have more days with us.
	
And that's the whole idea. We will use a Max Heap to keep track of all the courses we have taken so far. The max heap will order those courses by their "duration" or "number of days required to finish".

And so, at any time when we cannot take the current course, we can check if we can undo the course on top of the maxHeap and instead do the current course. If we can, then we will remove the course on top of the maxHeap and instead push the current course in the maxHeap and update the days spent so far accordingly.

And finally, the Max Heap will have the maximum number of courses that we can take.

You might also think that okay, if I undo a course on top of the maxHeap, how does that guarantee that we can finish current course before its deadline. Well, that's because the list is sorted by the deadline value. It means, the course that was on top of maxHeap had a deadline same or less than current course. And since we were able to complete that course, we can definitely complete current course before or at the deadline.