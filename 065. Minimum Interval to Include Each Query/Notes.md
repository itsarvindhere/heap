# PROBLEM STATEMENT

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

# EXAMPLE

    Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
    Output: [3,3,1,4]

Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

## **1. BRUTE FORCE APPROACH - TLE**

In the Brute Force Approach, for each query, we have to traverse the whole list to find the minimum interval size. This is not efficient and hence, we will get TLE.
		
## **2. USING A MINHEAP**

What if the intervals were sorted based on their start time? Then, all those intervals for which the start value is already > query are of no use and we should not waste our time checking them. So that means, as soon as we reach an interval for which "start" > "query", we know that not just that interval, but all the intervals after it are also not valid so no need to waste time checking them. 

This also means, all the intervals for which "left" <= "query", may contain the "query". Why did I say "may contain"? Because  it is also possible that while left <= query, the right is not >= query. 

	Suppose we have interval = [1,5] and query = 6

	Then, we know that since 1 <= 6, it is possible that "6" may be in this interval
	
	But after we see that "5" < "6", we know this interval is not at all valid and "6" is not in it. 
	
And that's the idea of the Min Heap approach. We will use a MinHeap because we are looking for the minimum size of an interval that contains the "query". So, first, we will simply push all those intervals in the MinHeap which we think could contain the point "query". 

And once we are done, we will then remove all those intervals from the top for which "right" > "query". 

And now, on the top of heap, we will be left with the smallest interval size since this is a Minheap and so, smallest size will be on top.

Also, as the elements in heap are to be placed based on the size, that means, we have to push a pair in the heap -> (size, right).

And since we want ouput array to have value for the original query index, we also need to keep track of the original index of each query. Hence, before soring the query array, we have to convert each value to a pair (query, queryIndex). 









