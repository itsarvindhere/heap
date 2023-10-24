# PROBLEM STATEMENT

You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 

# EXAMPLE

    Input: nums = [6,3,3,2], k = 2
    Output: 216

Explanation: Increment the second number 1 time and increment the fourth number 1 time.
Now nums = [6, 4, 3, 3], with a product of 6 * 4 * 3 * 3 = 216.
It can be shown that 216 is maximum product possible, so we return 216.

Note that there may be other ways to increment nums to have the maximum product.

# APPROACH

It is pretty evident if you take some examples that it is always optimal to increment the smallest number in the list by 1 in each operation so that the overall product is maximized.

So, we can use a minHeap to get the smallest element in the list at any time, increment it by 1, and push it back in the minHeap.

And finally, we just need to return the product of all the numbers in minHeap.