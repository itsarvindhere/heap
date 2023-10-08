# PROBLEM STATEMENT

In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

# EXAMPLE

    Input: barcodes = [1,1,1,1,2,2,3,3]
    Output: [1,3,1,3,1,2,1,2]

# **1. USING A MAX HEAP - O(NLogN)**
There are some other problems that are exactly the same as this one. 

For example, this one -> https://leetcode.com/problems/reorganize-string/

Here is my solution for the Reorganize String problem - https://leetcode.com/problems/reorganize-string/discuss/3950220/Python-Simple-Max-Heap-Solution

The same logic can be used in this problem.

Since we are asked to arrange the barcodes such that no two barcodes are the same, the most optimal way to ensure this is to give priority to the barcodes that occur most number of times. 

	For example, if we have barcodes = [1,1,1,1,2,2,2,3,3]
	
	We should give priority to "1"
	
	Because, between two "1s" we can put 2 or 3 so that two "1" are not together
	
	If we don't give priority to "1" then definitely we will get two 1s together at the end.
	
	Now the question is, between two "1", what should we put?
	
	We should put the barcode that occurs "second" most number of times after "1" at that moment.
	
	So initialy, frequencies are {1 : 4, 2 : 3, 3: 2}
	
	We take "1" first since it occurs most number of time
	output = [1]
	
	Now, frequencies are {1 : 3, 2 : 3, 3: 2}
	
	Now, we cannot take "1" again so we should now take "2" since 2 is the second most occuring barcode
	output = [1,2]
	
	Now, frequencies are {1 : 3, 2 : 2, 3: 2}
	
	Now, we can  take "1" again as it is the most occuring at this point
	output = [1,2,1]
	
	Now, frequencies are {1 : 2, 2 : 2, 3: 2}
	
	Now, we cannot  take "1" again but we can either take "2" or "3". 
	No matter what we take since both have same frequency at this point
	Let's take "3"
	output = [1,2,1,3]
	
	Now, frequencies are {1 : 2, 2 : 2, 3: 1}
	
	Now, we can  take "1" again as it is the most occuring at this point
	output = [1,2,1,3,1]
	
	Now, frequencies are {1 :1, 2 : 2, 3: 1}
	
	Now, we take "2" since it is the most occuring at this point
	output = [1,2,1,3,1,2]
	
	Now, frequencies are {1 :1, 2 : 1, 3: 1}
	
	Now, we can either take "1" or "3" but we cannot take "2" here
	Let's take "1"
	output = [1,2,1,3,1,2,1]
	
	Now, frequencies are {1 :0, 2 : 1, 3: 1}
	
	Now, we can either take "2" or "3". 
	Let's take "3"
	output = [1,2,1,3,1,2,1,3]
	
	Now, frequencies are {1 :0, 2 : 1, 3: 0}
	
	And finally, the only value we can take now is "2"
	output = [1,2,1,3,1,2,1,3,2]
	
	And that's the required output
	
Do note that there can be multiple solutions for a test case. 

As we saw in the example, we need to keep track of what was the most occuring element at any point. Also, if we cannot take it at that point, we have to take the second most occuring element at that point.

So, a data structure that we can use for this is a Max Heap. So, it will order elements based on their frequency from maximum to minimum and as we push the elements with new frequencies to this maxHeap, it will keep updating the order automatically.

# **2. OPTIMAL SOLUTION - O(N)**

Instead of using a heap to keep track of the first and second most occuring element, we can use a simple list of size "N". Why?

See, we are ordering elements by their "frequency", right? And for any list of size "N", an element in that list can occur at least 1 time or at most "N" times. 

So, we can create an "N" sized list where each index represents the frequency (0-indexed so index "0" means frequency of 1) and each value will be a list that contains all those elements that have the particular frequency.

	Taking the same example as above => barcodes = [1,1,1,1,2,2,2,3,3]

	For this, the list will be like - 
	
	freqList = [[], [3], [2], [1], [], [], [], [], []]
	
	Here, at index 1, we have a list with element "3" in it.
	
	Index 1 represents a frequency value of "2"
	
	It means the element "3" occurs twice in the input list.
	
	So, that's how this list will work.
	
	And now, to keep track of the first and second greatest elements, we can use simple two pointers, i and j.
	
	There is no need to sort since the indices/frequencies are already ordered in increasing order.
	
	So, initially, both i and j point to the last index. Now, there may or may not be an element in that last index list.
	
	And that could be the case for any index. 
	
	So, in each iteration of our loop, we will check if at "i" and "j" we have an empty list
	
	If yes, we will decrement them accordingly so that they point to an index that has some values.
	
	And do note that it is  possible to have "i" and "j" pointing to same index 
	because there can be multiple elements with the same frequency at any time.
	
	So, in that case, the first and second greatest elements will have same frequency.
	
And finally, the logic is pretty simple. In fact, I made sure to write it in the same way as for heap approach.
	
So, first we will get the "i" list's last element as that would be the one that's most occuring at that point.

If it is same as previous, we will then get the "j" list's last element instead. 

And as we keep putting elements in output list, we will also keep putting those elements back in the "freqList"  but at the "prevIndex - 1" location since we used them once.