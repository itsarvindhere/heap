# PROBLEM STATEMENT

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

 - choose an index i such that 0 <= i < nums.length,
 - increase your score by nums[i], and
 - replace nums[i] with ceil(nums[i] / 3).

Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

# EXAMPLE

    Input: nums = [1,10,3,3,3], k = 3
    Output: 17

Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.

The final score is 10 + 4 + 3 = 17.

# APPROACH

It is really easy to figure out that we need a heap in this problem.

The problem asks us to pick a number in each iteration and add it to the score. And it also asks us to have the maximum possible score. So, it simply means, in each operation, pick the greatest number available with us. And here, we can use a maxHeap just for that because a maxHeap orders the elements from greatest to smallest and at any time, we can get the greatest element at that time.

The rest, is a pretty straightforward logic.