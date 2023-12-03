from heapq import heappush, heappop
def kthSmallest(mat, k: int) -> int:
        
        # Max Heap to keep the sums
        # Fill it with the first row
        sums = []
        for num in mat[0]: heappush(sums, -num)
        
        # Number of rows
        rows = len(mat)
        
        # Number of columns
        cols = len(mat[0])
        
        # For each row
        for i in range(1,rows):
            
            # New Max Heap
            currSums = []
            
            # Go over each sum calculated so far
            for val in sums:
                
                # Go over each column
                for j in range(cols):
                    
                    # New Sum
                    newSum = (-val) + mat[i][j]
                    
                    # Push the new sum to the "currSums" maxHeap
                    heappush(currSums, -newSum)
                    
                    # If heap Size exceeds "k", pop from the top
                    if len(currSums) > k: heappop(currSums)

            # Update the "sums" maxHeap to the "currSums" maxHeap
            sums = currSums
        
        # Finally, from all the sums we have, return the kth smallest
        # That is, the "sum" on top of maxHeap
        return -sums[0]

mat = [[1,10,10],[1,4,5],[2,3,6]]
k = 7
print("Output ->", kthSmallest(mat,k))