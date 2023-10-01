from heapq import heappop, heappush
def getBiggestThree(grid):
        
        # MinHeap so that we can discard all the smaller sums and only have the three largest sums
        # We will maintain the heap size as "3"
        minHeap = []
        
        # Since we want distinct rhombus sums
        # We will use a set to make sure we are not adding those sums to the minHeap that we have already considered
        distinctSums = set()
        
        # Number of rows
        m = len(grid)
        
        # Number of columns
        n = len(grid[0])
        
        # For each row
        for i in range(m):
            # Go over each column
            for j in range(n):
                
                # The current cell is grid[i][j]
                # A single cell can also be considered
                # If the sum if not added already, add it to the minHeap
                if grid[i][j] not in distinctSums: 
                        
                    # Add it to the minHeap
                    heappush(minHeap, grid[i][j])
                    
                    # Add it to the distinct set
                    distinctSums.add(grid[i][j])
                        
                    # If heap size exceeds 3, pop from the top
                    if len(minHeap) > 3: heappop(minHeap)
                
                # Now, From this cell, 
                # can we create one or more rhombuses by going up and down diagonally?     
                
                # Consider this cell to be the left corner of the rhombus
                # We have four sides basically and we have to keep track of the sum of these four sides
                # 1. left corner to top corner
                # 2. left corner to bottom corner
                # 3. top corner to right corner
                # 4. right corner to bottom corner
                
                # The minimum rhombus size can be of four cells
                # So, let's initialize the indices for all the corner cells of the rhombus
                
                # Row and Column indices of the left corner
                leftCornerRow = i
                leftCornerCol = j
                
                # Row and Column indices of the top corner
                topCornerRow = i - 1
                topCornerCol = j + 1
                
                # Row and Column indices of the right corner
                rightCornerRow = i
                rightCornerCol = j + 2
                
                # Row and Column Indices of the bottom corner
                bottomCornerRow = i + 1
                bottomCornerCol = j + 1
                
                # Make sure these corner indices don't go out of bounds
                while topCornerRow > -1 and topCornerCol < n and rightCornerCol < n and bottomCornerRow < m and bottomCornerCol < n:
                    
                    # To Keep track of the sum of the current rhombus
                    rhombusSum = 0
                    
                    # 1. Sum of the side between leftCorner and topCorner
                    row = leftCornerRow
                    col = leftCornerCol
                    
                    while row >= topCornerRow and col <= topCornerCol:
                        rhombusSum += grid[row][col]
                        row -= 1
                        col += 1
                        
                    # 2. Sum of the side between topCorner and rightCorner
                    row = topCornerRow
                    col = topCornerCol
                    
                    # Do note that we already included the grid[topCornerRow][topCornerCol] in the sum above
                    # So, just to avoid adding this cell twice to rhombusSum, let's reduce it once here
                    rhombusSum -= grid[row][col]
                    
                    while row <= rightCornerRow and col <= rightCornerCol:
                        rhombusSum += grid[row][col]
                        row += 1
                        col += 1
                        
                    # 3. Sum of the side between rightCorner and bottomCorner
                    row = rightCornerRow
                    col = rightCornerCol
                    
                    # Do note that we already included the grid[rightCornerRow][rightCornerCol] in the sum above
                    # So, just to avoid adding this cell twice to rhombusSum, let's reduce it once here
                    rhombusSum -= grid[row][col]
                    
                    while row <= bottomCornerRow and col >= bottomCornerCol:
                        rhombusSum += grid[row][col]
                        row += 1
                        col -= 1
                        
                        
                    # 4. Sum of the side between bottomCorner and leftCorner
                    row = bottomCornerRow
                    col = bottomCornerCol
                    
                    # Do note that we already included the grid[bottomCornerRow][bottomCornerCol] in the sum above
                    # So, just to avoid adding this cell twice to rhombusSum, let's reduce it once here
                    rhombusSum -= grid[row][col]
                    
                    while row >= leftCornerRow and col >= leftCornerCol:
                        rhombusSum += grid[row][col]
                        row -= 1
                        col -= 1
                        
                    # Do note that we already included the grid[leftCornerRow][leftCornerCol] in the sum initially
                    # So, just to avoid adding this cell twice to rhombusSum, let's reduce it once here
                    rhombusSum -= grid[leftCornerRow][leftCornerCol]
                    
                    # If the sum if not added already, add it to the minHeap
                    if rhombusSum not in distinctSums: 
                        
                        # Add it to the minHeap
                        heappush(minHeap, rhombusSum)
                    
                        # Add it to the distinct set
                        distinctSums.add(rhombusSum)
                        
                        # If heap size exceeds 3, pop from the top
                        if len(minHeap) > 3: heappop(minHeap)

                    # And now, to move to the next rhombus, we will update the indices of the corners
                    # Left corner remains the same
                    
                    # Top corner gets updated
                    topCornerRow -= 1
                    topCornerCol += 1
                    
                    # Right Corner's row remains same but the column gets updated
                    rightCornerCol += 2
                    
                    # Bottom Corner gets updated
                    bottomCornerRow += 1
                    bottomCornerCol += 1
                    
                    
        # Output to return
        output = []
        while minHeap: output.append(heappop(minHeap))
        output.reverse()

        # Return the three largest Rhombus Sums
        return output


grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]

print("Output -> ", getBiggestThree(grid))