# PROBLEM STATEMENT

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

 - The 1st place athlete's rank is "Gold Medal".
 - The 2nd place athlete's rank is "Silver Medal".
 - The 3rd place athlete's rank is "Bronze Medal".
 - For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

# EXAMPLE

    Input: score = [10,3,8,9,4]
    Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

# APPROCH

Both Sorting and Heap approaches are O(NLogN) and pretty straightforward. 

In Sorting approach, we sort the scores in descending order and then populate the ranks accordingly.

In Heap approach, we use a Max Heap so that the top always has the highest score at any time. And then populate the ranks accordingly.