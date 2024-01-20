# PROBLEM STATEMENT

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

 - For example, for arr = [2,3,4], the median is 3.
 - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

 - MedianFinder() initializes the MedianFinder object.
 - void addNum(int num) adds the integer num from the data stream to the data structure.
 - double findMedian() returns the median of all elements so far. 
  
Answers within 10-5 of the actual answer will be accepted.

# EXAMPLE

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]

Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

# **1. USING SORTEDLIST**
This one is short and easier to understand.

We can import the "SortedList" from the sortedcontainers library.

As the name suggests, a SortedList maintains the order of elements as you put elements in it. It will automatically arrange them in the right order. So all that we need to do is the return the median, depending on whether we have odd number of elements or even.


# **2. USING TWO HEAPS**
I knew that we would need two Heaps but couldn't come up with a proper solution.

But this video helped me in understanding the approach - https://youtu.be/itmhHWaHupI

Basically, we will use two Heaps in this approach. Why a Heap and not a simple list? Because, using a Heap means that we would not have to care about ordering the elements propertly as we insert them.

What we will do is, we will try to insert elements in the two heaps such that, at any time, if we want the median, we can get that from the top of any of the two heaps.

For example, let's say we have elements inserted as 1,2,3, and 4

In this case, one heap should be having elements as [1,2] and the other should have [3,4]. And at this point, if we are asked to find the median, then we can simply take "2" from first heap and "3" from the other. 

So, we can also now understand that the first heap needs to be a "MAX HEAP" so that the element on the top is the maximum element among all the elements in this heap.

Similarly, the second heap needs to be a "MIN HEAP" so that the element on the top is the minimum element among all the elements in this heap.

Another thing to take care of is the sizes. We know that at any time, the number of elements inserted so far can either be even or odd. When it is even, both the heaps will have same number of elements. But, when the number of elements inserted so far as odd, we know that one heap will have one extra element than the other. And we will allow that because we cannot do anything in this case. 

But, this also means that the difference in lengths of both these heaps can be at most 1. If one heap has one element, then the other can have at most two elements, not more than that. Because, we want to make sure sizes are almost the same for both heaps.

Finally, since we have already established that if the ordered list is like [1,2,3,4], then the first heap (MAX HEAP) will have [1,2] and second heap (MIN HEAP) will have [3,4], this means - 

	The maximum element in Max Heap cannot be greater than the minimum element in the Min Heap

	If this is not the case, we have to correct the order by moving this greater element from the Max Heap to Min Heap

And that's the whole logic. 




















