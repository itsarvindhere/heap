def kthSmallest(matrix, k: int) -> int:
        # Length of the matrix
        n = len(matrix)
        
        # MATRIX ELEMENTS
        matrixList = []
        
        # Put the elements of matrix in the list
        for i in range(n):
            for j in range(n):
                matrixList.append(matrix[i][j])
                
        # Sort the list
        matrixList.sort()
        
        # Return the kth element
        return matrixList[k - 1]



matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print("Output -> ", kthSmallest(matrix,k))