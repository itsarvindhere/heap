# PROBLEM STATEMENT

You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

 - Choose the pile with the maximum number of gifts.
 - If there is more than one pile with the maximum number of gifts, choose any.
 - Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.


Return the number of gifts remaining after k seconds.

# EXAMPLE

    Input: gifts = [25,64,9,4,100], k = 4
    Output: 29

Explanation: 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

# **1. BRUTE FORCE APPROACH**

In the Brute Force approach, in each second, we will have to traverse the whole list again to get the new maximum index.

# **2. HEAP APPROACH**
Since at each second, we want the maximum value in the list, there is one data structure that we can use. It is the Max Heap. So, instead of looping over the list again and again at every second to get the maximum at that point, we let heap do this for us. So, as we push into or pop from the heap, the heap will reorder the elements such that the top of the heap always has the maximum value. 
​
Note that in Python, there is no standard Max Heap implementation. So, we can use a Min heap but when we push elements, we will first change their signs and then push them which lets us use the MinHeap as a MaxHeap in Python.