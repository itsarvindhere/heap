from heapq import heappush, heappop
def trapRainWater(heightMap) -> int:
        
        # Rows
        rows = len(heightMap)
        
        # Columns
        cols = len(heightMap[0])
        
        # How much water is trapped
        waterTrapped = 0
		
        # Since we always want to check the smallest height among the boundary cells, we can use a MinHeap for that
        minHeap = []
        
        # A 2D list to keep track of the visited or non visited state of each cell
        # We can simply denote visited cells by "1" and non visited ones by "0"
        visited = [ [0]*cols for i in range(rows)]
        
        # Take the boundary cells and push them in the minHeap with their height
        
        # First, push the boundary cells in the first row and last row to the minHeap
        for i in range(cols):
            
            # First Row Cells
            heappush(minHeap, [heightMap[0][i], 0, i])
            
            # Last Row Cells
            heappush(minHeap, [heightMap[rows - 1][i], rows - 1, i])
            
            # Also mark them as visited since we know boundary cells cannot hold any water at all
            visited[0][i] = 1
            visited[rows - 1][i] = 1
        
        # Next, push the boundary cells in the first column and last column to the minHeap
        for i in range(rows):
            
            # First Column Cells
            heappush(minHeap, [heightMap[i][0], i, 0])
            
            # Last Column Cells
            heappush(minHeap, [heightMap[i][cols - 1], i, cols - 1])
            
            # Also mark them as visited since we know boundary cells cannot hold any water at all
            visited[i][0] = 1
            visited[i][cols - 1] = 1
            
        
        
        # Now, we can start the main logic
        while minHeap:
            
            # Get the boundary cell with the smallest height from top of minHeap
            top = heappop(minHeap)
            
            # Row and column of this cell
            row, col = top[1], top[2]
            
            # Now, we want to check its neighbors and see if those can hold any water or not
            # For any cell, it has at most 4 neighbors - above it, on left side of it, on right side of it and below it
            
            neighbors = [[row, col - 1], [row, col + 1], [row - 1, col], [row + 1, col]]
            
            for i,j in neighbors:
                    
                # Make sure we check only the valid cells where row and column value is not out of bounds
                # Also, the cell shouldn't be visited already
                if i >= 0 and i < rows and j >= 0 and j < cols and visited[i][j] != 1:
                    
                    # Can this cell store water?
                    # The only way to store water is if this cell has a smaller height than the "top" cell
                    if heightMap[i][j] < top[0]: 
                        
                        # How much water it can hold? That is equal to the difference in the heights of the two
                        waterTrapped += top[0] - heightMap[i][j]
                        
                        # If this cell has a height < height of the boundary cell
                        # Then after water is trapped, its new height will be equal to the boundary cell
                        heappush(minHeap, [top[0], i, j])
                        
                    else:
                        
                        # If this cell has a height >= height of the boundary cell
                        # Then no water can be trapped, so its height remains the same as before
                        heappush(minHeap, [heightMap[i][j], i, j])
                            
                    # We will mark this cell as visited since we already checked it
                    visited[i][j] = 1
                    
        # Return the amount of water trapped
        return waterTrapped

heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]

print("Output -> ", trapRainWater(heightMap))