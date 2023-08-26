# PROBLEM STATEMENT

You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.

# EXAMPLE

    Input: matrix = [[5,2],[1,6]], k = 1
    Output: 7

Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.

# **1. BRUTE FORCE SOLUTION - TLE**

In Brute Force approach, for every cell, we have to go through each cell matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n

Here, we are doing unnecessary computations again and again which can be avoided if we precompute certain data.

# **2. PREFIX XOR + SORTING APPROACH**

To optimize the Brute Force solution, we first have to understand what computation is getting repeated unnecessarily.

For that, let's take an example.

	10 9 5
	2  0 4
	1  0 9
	3  4 8
	
Here, we have m = 4 and n = 3 so there are four rows and three columns.

Now, let's take each cell and see how we will compute its value.

	val(0,0) => 10
	val(0,1) => 10 ^ 9 => 3
	val(0,2) => 10 ^ 9 ^ 5 => 6
	val(1,0) => 10 ^ 2 => 8
	val(1,1) => 10 ^ 9 ^ 2 ^ 0 => 1
	val(1,2) => 10 ^ 9 ^ 5 ^ 2 ^ 0 ^ 4 => 0
	val(2,0) => 10 ^ 2 ^ 1 => 9
	val(2,1) => 10 ^ 9 ^ 2 ^ 0 ^ 1 ^ 0 => 0
	val(2,2) => 10 ^ 9 ^ 5 ^ 2 ^ 0 ^ 4 ^ 1 ^ 0 ^ 9 => 8
	val(3,0) => 10 ^ 2 ^ 1 ^ 3 => 10
	val(3,1) => 10 ^ 9 ^ 2 ^ 0 ^ 1 ^ 0 ^ 3 ^ 4 => 7
	val(3,2) => 10 ^ 9 ^ 5 ^ 2 ^ 0 ^ 4 ^ 1 ^ 0 ^ 9 ^ 3 ^ 4 ^ 8 => 7
	
	
 Here, you will see that some computation is getting repeated. 
 
 If you still cannot figure it out, let me make it more clear - 
 
	val(0,0) => 10
	val(0,1) => val(0,0) ^ matrix[0][1] => 3
	val(0,2) => val(0,1) ^ matrix[0][2] => 6
	val(1,0) => val(0,0) ^ matrix[1][0] => 8
	val(1,1) => val(0,1) ^ matrix[1][0] ^ matrix[1][1] => 1
	val(1,2) => val(0,2) ^ matrix[1][0] ^ matrix[1][1] ^ matrix[1][2] => 0
	val(2,0) => val(1,0) ^ matrix[2][0] => 9
	val(2,1) => val(1,1) ^ matrix[2][0] ^ matrix[2][1] => 0
	val(2,2) => val(1,2) ^ matrix[2][0] ^ matrix[2][1] ^ matrix[2][2] => 8
	val(3,0) => val(2,0) ^ matrix[3][0] => 10
	val(3,1) => val(2,1) ^ matrix[3][0] ^ matrix[3][1] => 7
	val(3,2) => val(2,2) ^ matrix[3][0] ^ matrix[3][1] ^ matrix[3][2] => 7
	
	
So, for each cell (except the cell of the first row), the value can be computed as the (value in the cell above it ^ the xor of all values in current row so far)

We can precompute the xor of all the values in each row by converting the input matrix into a prefix xor matrix such that at each cell, the value represents the XOR in that row so far.

So, the example that we took will be converted to -

	10 3 6
	2  2 6
	1  1 8
	3  7 15
	
	 Now, matrix[1][1] = 2 means that at the cell (1,1), the prefix xor is 2. 

Finally, the last step is to put everything together and use our prefix XOR to find the value for any cell.

As we saw, for the first row, the value of each cell is simply the prefix XOR at that point.

But for each row after that, the value will be (value of the cell on top ^ prefix xor so far)

And since we want the kth largest XOR value, we can sort the list of XOR values and return the kth largest value.

# **3. PREFIX XOR + MIN HEAP APPROACH**
Since all we care about is the kth largest XOR value, we might be unnecessarily sorting the data in most of the test cases which will be of no use. So, we can take a minHeap instead and let it handle the ordering. All we will do is make sure heap size does not exceed "k" so at the end, the top of the heap will be the kth largest XOR value.






