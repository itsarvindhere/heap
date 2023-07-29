# PROBLEM STATEMENT

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
# EXAMPLE

    Input: nums = [3,4,5,2]
    Output: 12 

Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

# **1. BRUTE FORCE SOLUTION - O(N^2)**

The Brute Force approach is pretty simple. For every index, we will go through every other index on its right and see which multiplication result is the largest and then update the output accordingly. Finally, we will get the largest possible product of two numbers in the list.

# **2. SORTING SOLUTION - O(NLogN)**
If we think a bit, we see that since we want the maximum possible product of two numbers, those two numbers need to be the two greatest numbers of the list.

Hence, we can sort the input list and then return the product of the two greatest numbers.

# **3. HEAP SOLUTION - O(NLogK)**

Since we just want the "2" greatest numbers in the list, we can find the more efficiently using a Heap. We will maintain a heap of size "2" and this will be a minHeap so that we can discard all the smaller elements and at the end, our heap will have only two elements - the two greatest elements in the list.

Here, Time complexity is "NLogK" because here, K = 2, the size of the heap. We will never let heap size exceed 2 and if it does, we will bring it back to size "2" by popping off that one extra element from top.

# **4. BEST SOLUTION - O(N)**

Since all that we want is the first greatest and the second greatest elements of the list, there is no need to Sort the list or use a Heap. Instead, we can do a simple one pass and find the first greatest and second greatest elements. In this way, there is no need to use any extra space and our solution will run in O(N) time complexity, making it the most efficient among all.