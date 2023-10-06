# NOTES

You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

# EXAMPLE

    Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    Output: 3

Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

# APPROACH

Whenever there is an Interval related problem where we need to take care of overlaps, Sorting is something we usually use to make it easier to check overlaps.

In this problem too, we will sort the input list based on the "left" value of the interval.

In this way, after sorting, for any two intervals, we can say that the interval on right definitely starts after or at the end of interval on left. Makes sense, right?

Suppose we have these two intervals after sorting - 

    [[1,5], [6,10]]

Here, the interval on right starts after the interval on left has ended. So there is no overlap. So these two can go in the same group.

But, if the intervals are like 
    
    [[1,5], [4,10]]
    
Then we see that interval on right starts before the interval on left has ended. So, there is an overlap so these two cannot go in same group.

So, as per the problem, they should belong to two separate groups.

But, now the question is, for the right interval, should we create a new group or put it in some other group that already exists?

Let's take another example for that - 

    [[2,4], [3,7], [5,6]]

Here, initially, the interval [2,4] will go in a new group.

Then, we have [3,7]. We see that it starts at "3" but the previous interval ends at "4". It means, there is an overlap. So, we will have to create a new group again.

Then, we have [5,6]. We see that it starts at "5" but the previous interval ends at "7" So there is an overlap. But, now comes the question of whether we should create a new group or put it in some existing group.

We can see that [5,6] can go in the group which has [2,4] because the "left" value "5" is greater than the "right" value "4". In simple words, [5,6] starts after [2,4] ends. So these two do not overlap.

Now, just think of a scenario where there are 1000s of intervals between [2,4] and [5,6] with which [5,6] overlaps. So how can we quickly find the interval with which [5,6] does not overlap?

We are comparing the "left" value of an interval with the "right" value of a previous interval to check for an overlap. Now, just assume we have some way to keep track of what is the smallest "right" value so far. If we have this data, we need to compare the current interval's "left" value to that smallest "right" value. And if there is no overlap, we can group them together.

But, if there is an overlap, we can be sure that all other intervals also overlap because this is the smallest "right" value so all other intervals that we have traversed so far will have "right" values equal or greater to this smallest "right" value.

In the example above 

    [[2,4], [3,7], [5,6]]

When we are at [5,6] the smallest "right" value so far is "4" And we see that "left" value of [5,6] is "5". 

Since 5 > 4 it means whatever interval has the "right" value of "4" is non-overlapping with [5,6] and so both can be placed in the same group.

And now, we no longer need to keep track of "4". Why?

Again, that's because we have already sorted the list. So, any interval that is coming after [5,6] will have "left" value >= 5 only. So, that interval will definitely start after the interval [2,4] has ended. But, keeping "4" as smallest at that time as well can increase our problems because just think of this case - 

    [[2,4], [3,7], [5,6], [5,8]] 

Till [5,6] we have the smallest "right" value as "4"

And we see that [5,6] and [2,4] can be in the same group.

Now, if we do not update this smallest "right" value, then even [5,8] also is non overlapping with [2,4]. So, by our logic, the group will contain [2,4], [5,6] and [5,8] which is not right. Because [5,6] and [5,8] overlap, even though [2,4] and [5,8] don't. The reason is [5,8] starts before [5,6] has ended.

It means, as soon as we had grouped [5,6] and [2,4] together, we should've no longer considered [2,4] and updated our smallest "right" value to "6" (Since it is the next smallest after "4" among all the intervals we have traversed so far).

So, as soon as we group two interval together, we no longer care about the interval with the smallest "end" value anymore. Since we don't care about it, we should now quickly get the next smaller "end" value so far.

So, to keep track of the smallest "right" value so far that we can compare with the current "left" value, we can use a minHeap. And even if we remolve the smallest value from top, we can get the next smallest again from the top.

And that's the whole idea of the minHeap solution.

