# PROBLEM STATEMENT

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

# EXAMPLE

    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2

Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

# APPROACH

This problem is just a variation of the Problem -> https://leetcode.com/problems/sort-characters-by-frequency/

Here is my solution for that problem where I used the same three methods -> https://leetcode.com/problems/sort-characters-by-frequency/discuss/3893835/Python-Sorting-Heap-and-Bucket-Sort-Solutions

In this problem, we want the minimum length set of elements that if we remove from the input list, the input list is reduced to at least half of its original length.

So, it makes sense to choose those elements to remove first which are occuring the most number of times in the list.

	For example, if arr = [3,3,3,3,5,5,5,2,2,7]
	Half length is 5

	Here, it is better to remove all occurance of "3" first which makes the list [5,5,5,2,2,7]
	But still, length of list is 6 but we are still not at half length.
	Then, we remove all occurances of "5" to make the list [2,2,7]
	Now, length is 3 and so, we already removed enough elements to make length >= half

	Hence, the minimum length of set is "2". It is not possible to have a set of length 1 in this case.
	
So, what we want is to order the elements by their frequencies.

There are three different ways to do that. We can either create a frequency List by sorting the elements based on their frequency, or use a maxHeap so that the heap takes care of the ordering, Or use bucket sort. We can use bucket sort here because each element can occur at most "n" times. So, we can have a list of length n, where each index represents the frequency. For example, index = 0 means frequency = 1 (Since indices start from 0).

And at each index, we will have a bucket that groups the elements with same frequency together. And now, we don't have to manually sort this list because indices are already in sorted order.