# PROBLEM STATEMENT

You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

# EXAMPLE

    Input: events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
    Output: 5

    Explanation: You can attend all the five events.

    Attend the [1,5] event on day 1.
    Attend the [2,3] event on day 2.
    Attend the [2,3] event on day 3.
    Attend the [1,5] event on day 4.
    Attend the [1,5] event on day 5.

# APPROACH

To understand how can we optimally choose an event to attend, take this example - 

	[[1,5],[1,5],[1,5],[2,3],[2,3]]
	
See, the most basic thing that comes to mind when we start solving this problem is to simply sort the events by their start days and then, at any day, simply attend an event at the earliest possible available day. And this approach will work for some test cases. 

For example,
	
	If we take [[1,2],[2,3],[3,4]]
	
	Then, these are sorted by their start days already.

	So, at Day 1, we can attend event [1,2]
	At day 2, we can attend event [2,3]
	And at day 3, we can attend [3,4]
	
	
	But now, take the example [[1,5],[1,5],[1,5],[2,3],[2,3]]
	
	At day 1, we attend event [1,5]
	At day 2, we attend event [1,5]
	At day 3, we attend event [1,5]
	At day 4, we cannot attend any event
	At day 5, we cannot attend any event

	So, with this approach, we can only attend "3" events out of "5"
	
	But, there is a way to attend all "5" events in "5" days
	
	At day 1, we attend event [1,5]
	At day 2, we attend event [2,3]
	At day 3, we attend event [2,3]
	At day 4, we attend event [1,5]
	At day 5, we attend event [1,5]
	
	And in this way, we can attend all the five events in five days.

So, what did we understand from this test case?

We understood that at any day, the most optimal event to attend is the one that is ending first out of all the other events that we can choose from that day.

That's why, at day "2", we could attend [1,5], [1,5], [2,3] and [2,3]. And among all these, [2,3] and [2,3] are both ending at day "3". So, we can choose any one of them and attend that event. And it makes sense, right? Because we know that [1,5] is ending two days after [2,3] ends so it is possible that we might be able to attend [1,5] in the future. But right now, it makes more sense to attend [2,3].

And that's the whole idea of the solution.

For each day, we will see what are all the candidate events and then, we want to pick the event with the smallest "end" day value out of them. For this, we can use a minHeap. 