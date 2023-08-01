from heapq import heappop, heappush


def kWeakestRows(mat, k: int):
        
        # Rows
        m = len(mat)
        
        # Columns
        n = len(mat[0])
        
        # Since all that we want are the "k" weakest rows
        # We are unnecesarrily sorting the whole rowData list that we generate
        # I mean, just suppose if we have 100 rows and we have to get 2 smallest ones
        # In that case, we will sort 100 elements just to get the 2 smallest ones.
        # So, we are doing some unnecesary computation. 
        # We can use a heap here and maintain its size as "k"
        # So that as we keep adding each row's soldier count, it will automatically order that data from smallest to largest
        # And in the end, we will have "k" weakest rows
        # We want to discard all stronger rows so we will use a maxHeap here
        
        maxHeap = []
        
        # Go through each row
        for i in range(m):
            
            # Count of soldiers
            count = 0
            
            # Use Binary search
            
            # Index of rigtmost soldier in row after which all are civilians
            indexOfRightMostSoldier = -1
            
            start = 0
            end = n - 1
            
            while start <= end:
                
                mid = start + (end - start) // 2
                
                # If at "mid" we have a soldier
                # It may or may not be the rightmost soldier
                # So, we save its index and keep searching on right side of mid
                if mat[i][mid] == 1:
                    indexOfRightMostSoldier = mid
                    start = mid + 1
                    
                # If at "mid" we have a civilian, there cannot be a soldier on right
                # So, we search on left side of mid for the index of rightmost soldier
                else: end = mid - 1
            
            # If there are soldiers in this row, the index will not be -1
            if indexOfRightMostSoldier != -1: count = indexOfRightMostSoldier + 1
                    
            # Add the count and the index of the row in the heap
            # Note that we are passing a tuple of length 3
            # The first value is the count of soldiers (in negative because we want a maxHeap)
            # The second value is used to break the tie in case we have two rows with same count
            # We want the first "k" weakest rows, so it basically means if we have two rows with same count
            # Then the priority should be given to the row that came earlier
            # Hence, this tie breaker value will be a negative of the index
            # So it means if one row has index 1 and other has index 2
            # Then we know that -1 > -2 so, it will give priority to the row with "-1"
            # The third value is just the index of the row
            # Note that this won't work if you only provide a tuple of length = 2
            heappush(maxHeap, (-count, -i, i))
            
            # If size of heap exceeds k, remove element from top of heap
            if len(maxHeap) > k: heappop(maxHeap)
        
        # We need only the indices of the rows
        output = [-1] * k
        
        for i in range(k - 1, -1, -1): output[i] = heappop(maxHeap)[2]
            
        # Return the required data
        return output


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

print("Output -> ", kWeakestRows(mat,k))

