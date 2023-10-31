# PROBLEM STATEMENT

There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

# EXAMPLE

    Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
    Output: 7

Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.

# APPROACH

It is not difficult to figure out that this is a Greedy problem.

The most optimal way to eat the maximum number of Apples would be to eat those first that will rot first. Makes sense, right?

And so, at any time, for any day "i", from all the trees that are available at that day, we want to pick an apple from the tree for which its Apple(s) will rot the earliest. And so, we can use a MinHeap for that.

The rest, is pretty straightforward.