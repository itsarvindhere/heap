def kWeakestRows(mat, k: int):
        
        # Rows
        m = len(mat)
        
        # Columns
        n = len(mat[0])
        
        # In Brute Force approach, For each row, we are traversing the whole row to count the soldiers
        # Suppose if whole row has soldiers only. In that case, we will traverse the whole row
        
        # Since we already know that soldiers stand in front of civilians
        # It means, as soon as we encounter a civilian, there is no soldier on the right
        # So, basically, each row is in a sorted order
        # And so, to count soldiers, we can use Binary Search instead
        
        # Each data will be a pair (soldierCount, rowIndex)
        rowData = []
        
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
                    
            # Add the count and the index of the row in the rowData
            rowData.append((count, i))
            
        # Finally, sort the rowData in inreasing order based on count
        rowData.sort()
        
        # And finally, return the "k" weakest rows
        return [pair[1] for pair in rowData][:k]


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

print("Output -> ", kWeakestRows(mat,k))

