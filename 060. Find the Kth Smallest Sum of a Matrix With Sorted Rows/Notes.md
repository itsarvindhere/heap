# PROBLEM STATEMENT

You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.

You are allowed to choose exactly one element from each row to form an array.

Return the kth smallest array sum among all possible arrays.

# EXAMPLE

    Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
    Output: 9

Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  

# APPROACH

In this problem, all we care about are the "Sums of the arrays", not the actual arrays. This is important to keep in mind. 


	For example, if we have

	 mat = [[1,3,11],[2,4,6]], k = 5
	 
	 Now, if we write all the possible arrays that we can get -
	 
	 [1,2], [1,4], [1,6], [3,2], [3,4], [3,6], [11,2], [11,4], [11,6]
	 
	 So, the sums are -
	 
	 3,5,7,5,7,9,13,15,17
	 
	 If we sort these, we get - 3,5,5,7,7,9,13,15,17
	 
	 Since k = 5, the 5th smallest sum is "7"
	 
Now, as mentioned above, we care about the sums, not the arrays themselves. So, what we can do is, we can iterate over the rows and in each iteration, we update the sum that we have so far by also considering the elements of the new row.

	For example, mat = [[1,3,11],[2,4,6]], k = 5
	
	Since every matrix will have at least one row,
	
	If there are "n" columns, it means
	
	Every matrix will have at least "n" sum values. 
	
	For example, if we have mat = [[1,2,3]]
	
	Then, the sum values will be 1,2, and 3 if we pick at most one element from this row.
	
	So, we can initialize our Sum array with the first row of the given matrix.
	
	Now, we can iterate over the remaining rows, if they exist.
	
	And in each new iteration, we will go over that new row, 
	take each element and pair it with every element in the sum array so far.
	
	For example, for mat = [[1,3,11],[2,4,6]], k = 5
	
	Initially, sum = [1,3,11]
	
	Now, when we reach the second row [2,4,6]
	
	We basically need pairs like this - 
	
	[1 + 2, 1 + 4, 1 + 6, 3 + 2, 3 + 4, 3 + 6, 11 + 2, 11 + 4, 11 + 6]
	
	Or
	
	[3,5,7,5,7,9,13,15,17]
	
	And if we sort, then the new "sums" now becomes - 
	
	sums = [3,5,5,7,7,9,13,15,17]
	
And this way we can get all the sum values possible in the given matrix.
	
If there was one more row in this matrix, then we would've done the same with that. So, with the new values in sums list, we would've taken each value and paired it with each value of the new row.
	 
But, this is not an efficient approach.

Because, as we can see above, just for a small matrix with "2" rows and "3" columns, we had 9 sums possible. Or in other words, for an m x n matrix, there are m^n sum values possible.

Now, just imagine what would happen if there were 40 rows and 40 columns, that is, the worst case. Then, we would have 40^40 values which is a massive number and hence, we will get Memory Limit Exceeded Error.

So, it is important to note that "k" will be at most "200" in this problem for any test case, no matter how many rows or columns are there. So, even if we have a 40 x 40 matrix, there is no need to store all the sums. We just need to keep the k smallest sums. 

So, in any iteration, when we update "Sums", we just need the "k" smallest values. And with this optimization, our solution gets accepted.

# **1. SORTING APPROACH**
The Sorting Approach is pretty much what we discussed above. 

So, we have a "sums" list to keep the "k" smallest sums. It is initialized with the first row of the matrix.

Then, we loop over the rest of the rows, and in each iteration, we go over each element of the "sums" list and pair it with each element of the current row.

And then, whatever new array we get, we update "sums" to now point to this new array, just that we only want up to "k" smallest sum values.

# **2. MAX HEAP APPROACH**
Instead of first getting the sum valus and then sorting them and then getting the first "k" sums and assigning "sums" to them, for each row in each iteration, we can instead also use a Max Heap that will take care of ordering the sum values. 

All we need to care about is the size of Max Heap which should remain "k". In this way, at the end, Max Heap will have the kth smallest sum on the top.

