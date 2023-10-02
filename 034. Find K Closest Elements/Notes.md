# PROBLEM STATEMENT

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

# EXAMPLE

    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

## **1. MAX HEAP + SORTING APPROACH**

The simplest approach would be to use a maxHeap to keep the elements by their absolute difference with "x". We will maintain the size of the maxHeap as "k" so that in the end, we have the "k" closest elements with us.

And since we are asked to return the values in sorted order, we will need to sort the output list before returning it.


## **2. USING BINARY SEARCH**

Since the array is sorted already, the first thing that comes to mind is Binary Search!

We want the K closest element to x. So why not first find "THE" closest element to x.

Either it can be the element itself (if it is present in array) or it can be either the floor or the ceil.

And once we can find that particular element, that element will definitely be there in the output array which means we now have one less element to search for. 

Hence, we will use this closest element to get other closer elements to x. We can look at the right and left side of the closest element to see which one is closer. And increment or decrement the pointers accordingly.

I made sure to comment out each line so it is easy to understand what is going on in the code.









