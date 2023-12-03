def kthSmallest(mat, k: int) -> int:

        # Array to keep the sums
        sums = [0]
        
        # Number of rows
        rows = len(mat)
        
        # Number of columns
        cols = len(mat[0])
        
        # For each row
        for i in range(rows):
            
            # New Sums array
            currSums = []
            
            # Go over each sum calculated so far
            for val in sums:
                
                # Go over each column
                for j in range(cols):
                    
                    # Add the new sum to the currSums list
                    currSums.append(val + mat[i][j])
                    
            # Sort the currSums in increasing order (since we need to have sums in increasing order at the end)
            currSums.sort()

            # Update the sums list
            # We just care about "k" smallest sums
            sums = currSums[:min(k, len(currSums))]
        
        # Finally, from all the sums we have, return the kth smallest
        return sums[k - 1]

mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7
print("Output ->", kthSmallest(mat,k))