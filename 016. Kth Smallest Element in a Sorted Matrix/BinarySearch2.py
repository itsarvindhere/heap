# Helper method to count elements smaller than threshold
def countElements(matrix, threshold):
        
        n = len(matrix)
        
        # Count of Elements smaller than threshold in the matrix
        count = 0
        
        # The reason for the O(N^2) time complexity in the above Binary Search solution is
        # The nested for loop below
        # Since each row is sorted, we can apply Binary search on each row to get the rightmost element
        # That is <= threshold
        for i in range(n):
            
            start, end = 0, n - 1
            
            # Index of rightmost element that is <= threshold
            rightmostIndex = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                
                # If element at "mid" column in this row is <= threshold
                # Then all elements to its left are also <= threshold
                # But since we want rightmost element satisfying this condition
                # We keep searching on right side of mid
                if matrix[i][mid] <= threshold:
                    rightmostIndex = mid
                    start = mid + 1
                    
                # If element at "mid" column in this row is > threshold
                # This means, we cannot find any element on the right of mid
                # That is <= threshold since the row is sorted
                # So, we have to search on left side of mid
                else: end = mid - 1
            
            # If the row does not have any element that is <= threshold
            # Then rightmostIndex will be -1
            # For all other cases, increment count by "start"
            if rightmostIndex != -1: count += start
        
        # Finally, return the count of elements that are <= threshold
        return count

def kthSmallest(matrix, k: int) -> int:
        # Length of the matrix
        n = len(matrix)
        
        # There is a reason why the rows and columns are already in sorted order
        # And for the same reason, the problem asks us to write a solution with complexity better than O(N^2)
        # That reason is that we should use BINARY SEARCH in this problem
                
        # If k has the least value, that is, 1, then it means the smallst element in matrix
        # Since matrix is sorted already, kth smallest will be at the first row and first column
        
        # If k has the max value, that is n*n, then it means the largest element in matrix
        # Since matrix is sorted already, kth smallest will be at the last row and last column
        
        # So, the start of our search range is the element at first row and first column
        # And the end is the element at last row and last column
        # And we know that the kth smallest will lie in this range only
        
        start, end = matrix[0][0], matrix[n-1][n-1]
        
        while start <= end:
            
            # Mid
            mid = start + (end - start) // 2
            
            # Now, this "mid" may or may not exist in the matrix
            # But, using this, we can check if there are at least k elements on left side of mid
            # That are smaller or equal to mid
            # In that case, we can find the kth smallest on left side of mid

            count = countElements(matrix, mid)
            
            # If there are k or more elements that are smaller than "mid"
            # Then it means kth smallest element is on the left side of mid
            if count >= k: end = mid - 1
                
            # Otherwise, it means kth smallest is on the right side of mid
            else: start = mid + 1
        
        
        # Finally, "start" will be the kth smallest element
        return start



matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print("Output -> ", kthSmallest(matrix,k))