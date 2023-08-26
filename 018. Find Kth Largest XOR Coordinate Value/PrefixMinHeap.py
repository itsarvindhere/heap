from heapq import heappop, heappush


def kthLargestValue(matrix, k: int) -> int:

	# m and n
        m = len(matrix)
        n = len(matrix[0])
        
        # The reason why the above solution gives TLE is because
        # For each cell (a,b), we have to find XOR of every cell before where 0 <= i <= a < m
        # So, we are doing some repeated computation for every new cell
        # So, to reduce that extra work, we convert the input matrix into a prefix XOR matrix
        # So that for any cell, we can easily get the xor of values so far in its row.
        for i in range(m):
            xorSoFar = 0
            for j in range(n):
                xorSoFar ^= matrix[i][j]
                matrix[i][j] = xorSoFar
        
        # Min Heap
        minHeap = []
              
        # Once we have the prefix XOR, now we can apply the main logic
        for i in range(m):
            for j in range(n):
                
                # Value of current cell
                val = 0
                
                # If this is the first row
                # Just get the prefix xor value for the current cell
                if i == 0: val = matrix[i][j]
                    
                # Otherwise
                # The value for this cell will be 
                # The value for cell above it
                # ^
                # The xor Prefix so far in this current row
                else: val = matrix[i - 1][j] ^ matrix[i][j]
                
                # And once we have the value, we can update the matrix in place
                # Since later, we will only need this "val" for the cell (i,j)
                matrix[i][j] = val
                
                # And we also put the value in the minHeap
                heappush(minHeap, val)
                
                # If heap size exceeds k, pop
                if len(minHeap) > k: heappop(minHeap)

        # Return the "kth" largest Xor Value
        return minHeap[0]


matrix = [[10,9,5], [2,0,4], [1,0,9], [3,4,8]]

print("Output -> ", kthLargestValue(matrix, 4))