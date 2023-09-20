from heapq import heappop, heappush
def findDiagonalOrder(nums):
        # Output to return
        output = []
        
        # Min Heap to order elements by row + col sum
        minHeap = []
        
        # How many rows are there
        rows = len(nums)
        
        for i in range(rows):
            
            # How many columns are in current row
            cols = len(nums[i])
            
            for j in range(cols):
                
                # Push to minHeap
                heappush(minHeap, (i + j, -i, nums[i][j]))
        
        # Fill the output list with the data
        while minHeap: output.append(heappop(minHeap)[2])
        
        # Return the output list
        return output


nums = [[1,2,3],[4,5,6],[7,8,9]]

print("Output -> ", findDiagonalOrder(nums))
