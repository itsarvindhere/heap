from heapq import heappop, heappush


def kthSmallest(matrix, k: int) -> int:
        # Length of the matrix
        n = len(matrix)
        
        # Max Heap
        maxHeap = []
        
        # Put the elements of matrix in the list
        for i in range(n):
            for j in range(n):
                
                # Put the current element in the heap
                heappush(maxHeap,-matrix[i][j])
                
                # If heap size exceeds k, pop from the top of heap
                if len(maxHeap) > k: heappop(maxHeap)
                    
        # Return the kth smallest element
        return -maxHeap[0]



matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print("Output -> ", kthSmallest(matrix,k))