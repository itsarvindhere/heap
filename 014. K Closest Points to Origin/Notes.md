# PROBLEM STATEMENT

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# EXAMPLE

    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]

Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# **1. SORTING APPROACH - O(NLogN)**
Since we just want the "k" closest points, we can sort the points on the basis of their distance from origin in increasing order. In that way, the first "k" points in this sorted list will be the "k" closest points to origin.


# **2. MAXHEAP APPROACH - O(NLogk)**
The issue with the Sorting Approach is the unnecessary sorting that we are doing. Since we just want "k" closest points, we just have to care about the "k" smallest values, we should not care about sorting the values that we will not even need in the output. Here, we can take use of a maxHeap and we will fix its size as "k" such that as soon as its size exceeds "k", we will pop the top value.

And so, finally, we will have a maxHeap with only "k" elements in it and these will be the "k" closest points to the origin.

Why we used a maxHeap here? 

That's because we want to discard all the bigger distances and only have the smallest "k" distances. So, if we have a maxHeap, we can easily discard the bigger values from the top of heap as its size exceeds "k".
