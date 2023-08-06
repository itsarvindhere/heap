# PROBLEM STATEMENT

You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

# EXAMPLE

    Input: num = 1234
    Output: 3412

Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

# APPROACH

I don't think there is any difference in the overall time complexity when we compare both the solutions. Both are I think O(NLogN).

But, in the max Heap approach, you don't have to sort the even and odd list after you populate them with values. As we keep pushing values to maxHeap, it will automatically take care of order.

Also, in the max Heap approach, we don't need to keep track of the elements in individual even and odd lists using pointers since we can simply pop the top of the individual heaps and we know that will give us the greatest even or odd number at that time.