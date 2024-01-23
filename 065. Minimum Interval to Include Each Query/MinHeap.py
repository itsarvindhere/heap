from heapq import heappush, heappop
def minInterval(intervals, queries):
        
        # Number of queries
        n = len(queries)
        
        # Output List to return
        output = [-1] * n
        
        # The reason why the Brute Force approach failed is because of the inner for loop
        # Because, for every query, we have to iterate over the entire list of intervals
        # And that is very inefficient for large test cases
        # If we have all the intervals with us in which the value "query" exists
        # Then, we can use a MIN HEAP to get the interval with the least size out of those
        # But, what about those intervals that are invalid for some query? 
        # Should be just discard them? What if those are the ones in which some other queries exist?
        
        # For example, let's say that we have intervals as intervals = [[2,4], [1,4],[4,4],[3,6]]
        # Suppose the queries are [5,4,2]
        
        # SO, when we start with the query "5"
        # We will take a minHeap and put all those intervals in it which contain "5"
        # So, minHeap will have [[3,6]]
        # This means, we discarded all the other intervals
        # But, for the other queries, for example "2", those discarded intervals contained the solution
        # This problem should not exist if we start with the smallest value in "queries" list first
        # In other words, if the queries were sorted from smallest to largest
        # Then, this issue might not occur
        # Let's test that as well
        
        # Suppose, now the queries are [2,4,5] after we sorted them
        # Now, for the query "2" the minHeap will have [[2,4], [1,4]]
        # But now again, the other intervals are gone
        # And we know that for query "5", the interval that is smallest is the [3,6]
        
        # The solution for this is to sort the intervals as well, by their start values
        # Why?
        # Because, if the intervals are sorted by their start values, then, as soon as we reach an interval with start value > query
        # We know that not only that interval, but all the intervals after it are also not valid for the current query
        # But, for the upcoming query, we can continue checking because those intervals might become valid at that point
        
        # And that's the whole idea of this approach
        
        # A MIN HEAP
        minHeap = []
        
        # Sort queries in increasing order (keep track of their original indices as well)
        queries = [[queries[i], i] for i in range(n)]
        queries.sort()
        
        # Sort the intervals by start value
        intervals.sort()
        
        # Index to keep track of intervals in the intervals list
        idx = 0
        
        # Go over each query
        for query,i in queries:
            
            # Put all the intervals in the minHeap for which "left" <= queruy
            while idx < len(intervals) and intervals[idx][0] <= query:
                
                # We want the minHeap to order the intervals by their size
                heappush(minHeap, [intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1]])
                
                # Move to the next interval
                idx += 1
                
            # At this point, the minHeap has all the intervals for which "left" <= query
            # But, that doesn't mean all those intervals are valid
            # Because it is possible that while an interval has "left" <= query
            # The "right" is also < query. 
            # Because a valid interval should have "left" <= query and "right" >= query
            # Since intervals are sorted by their start values and so are queries
            # It means, if an interval is not valid for a query
            # It cannot be valid for any upcoming queries so we can discard it
            while minHeap and minHeap[0][1] < query: heappop(minHeap)
                
            # If minHeap is not empty, the top of minHeap has the most optimal interval for current query
            if minHeap: output[i] = minHeap[0][0]
                
        # Finally, return the output list
        return output

intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]

print("Output is ->", minInterval(intervals, queries))