# PROBLEM STATEMENT

You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

 - Each meeting will take place in the unused room with the lowest number.
 - If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
 - When a room becomes unused, meetings that have an earlier original start time should be given the room.

Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

# EXAMPLE

    Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
    Output: 0

Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 

# APPROACH

The approach is pretty straightforward. At any time, if we have any free rooms, we want to assign the current meeting to the room with the smallest number. So, we want the unused rooms to be ordered from smallest to largest at any time, so we use a Min Heap for them.

Similarly, if some rooms are currently in use, then we want to order them based on the time at which they will become free again from smallest to largest. And again, we will use a Min Heap for this.

We will traverse the meetings from left to right, based on their start values. Hence, we will sort them by their start values initially.

Finally, to keep track of how many meetings each room held, we can use a list of size "n" where each index represents a room.

The rest is pretty straightforward and each line is commented for easy understanding.