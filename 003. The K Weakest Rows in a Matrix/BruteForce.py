def kWeakestRows(mat, k: int):
        
        # Rows
        m = len(mat)
        
        # Columns
        n = len(mat[0])
        
        # In Brute Force solution, we will take each row, and count number of soldiers
        # And save the data regarding each row's soldier count
        # Finally, we will sort the rows based on soldier count
        
        # Each data will be a pair (soldierCount, rowIndex)
        rowData = []
        
        # Go through each row
        for i in range(m):
            
            # Count of soldiers
            count = 0
            
            for j in range(n):
                
                # If it is a soldier, increment count
                if mat[i][j] == 1: count += 1
                    
                # Otherwise, there are only civilians after this index so we can exit here
                else: break
                    
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

