def minInterval(intervals, queries):
        
        # Output List to return
        output = []

        # In Brute Force Approach
        # For each query, we will go over the entire list of intervals
        # And we will find the smallest one that contains the query
        
        for query in queries:
            
            # Size of the smallest interval for current query
            smallestIntervalSize = float("inf")
            
            # Go over the list of intervals
            for left,right in intervals:
                
                # If the current interval contains the value "query"
                # Then, check if it is the smallest interval or not
                if left <= query and right >= query:
                    
                    smallestIntervalSize = min(smallestIntervalSize, right - left + 1)
                    
            # Update the output list for the current query
            if smallestIntervalSize == float("inf"): output.append(-1)
            else: output.append(smallestIntervalSize)
                
                
        # Finally, return the output list
        return output

intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]

print("Output is ->", minInterval(intervals, queries))