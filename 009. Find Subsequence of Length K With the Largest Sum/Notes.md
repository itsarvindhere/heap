# PROBLEM STATEMENT

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# EXAMPLE

    Input: nums = [-1,-2,3,4], k = 3
    Output: [-1,3,4]

Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.

# APPROACH

The basic idea is that since we want a "k" length subsequence that gives us the maximum sum, it makes sense to choose the "k" greatest elements in the list. Only then we can get the greatest sum. So, this problem can be phrased as - 

	Given an input list, return the k largest elements in the same order as they occur in the original list.

So, since we want to keep the same order as in original list, we will need to keep track of the original indices of the values before we sort or put them in the heap.

And once we get the k largest values, we will then have to arrange them in the same order as they weer in the original list. That is, sort them again based on their indices.