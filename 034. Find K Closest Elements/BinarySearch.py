def findClosestElements(arr, k: int, x: int):

	# Length of the list
        n = len(arr)
        
        # Some edge cases
        # If "x" is smaller than even the smallest element in the list
        if x < arr[0]:
            # Simply return the first "k" elements
            return arr[:k]
        # If "x" is greater than even the greatest element in the list
        elif x > arr[-1]:
            # Simply return the last "k" elements
            return arr[k:]
        
        # Since the list is already in the sorted order
        # What if we can find the closest element to "k"?
        # If we can find the closest, we know that other closer elements are around this element only
        # For example, if we have arr = [1,2,3,4,5] and x = 3 and k = 4
        # The closest element to "3" is "3" itself at index 2
        # And so, we know that the other three elements closest to "3" are all on the left or right side of "3"
        
        # So first, we want the index of closest element to "x"
        # This, we can find using Binary Search
        closestElementIdx = -1
        
        start,end = 0, n - 1
        
        while start <= end:
            mid = start + (end - start) // 2
            
            # If at mid we found the element "x", then it is the closest
            # Doesn't matter if there are duplicates
            # Because later, we are anyways going to fetch all the closest elements around this index
            if arr[mid] == x:
                closestElementIdx = mid
                break
                
            # If the element at mid is greater than "x", search on the left side of mid
            if arr[mid] > x: end = mid - 1
                
            # If the element at mid is smaller than "x", search on the rigt side of mid
            else: start = mid + 1
        
        
        # In the end, we will have the closestElementIdx with us if the element "x" is present in the list
        # Otherwise, closestElementIdx will be -1
        
        # If the closestElement is -1, we need to assign it to either "start" or "end"
        # Whichever gives us the smaller difference with "x"
        # Note that if closestElementIdx is -1, then at this point, "start" will point to a bigger/equal element than "end"
        # Because binary search loop ended because start was no longer <= end
        # So basically, at this point, "start" points to ceil of "x" in the list
        # And "end" points to the floor of "x" in the list
        if closestElementIdx == -1:
            
            startDiff = abs(arr[start] - x)
            endDiff = abs(arr[end] - x)
            
            # Since "end" index is smallr than "start" index at this point
            # If the difference of "end" with "x" is <= difference of "start" with "x"
            # The closestElementIdx will be "end"
            closestElementIdx = end if endDiff <= startDiff else start
        
        # Now we have one less element to find
        k -= 1

        # We know that other closest elements lie on the left or right side of "closestElementIdx" only
        # So, let's try to find the boundary indices "left" and "right"
        # Such that, all the elements in between are the required "k" closest elements
        left = closestElementIdx - 1
        right = closestElementIdx + 1
        
        # While we haven't found all the required elements
        while k > 0:
            
            # If "left" is already out of bounds, increment "right"
            if left < 0: 
                right += 1
            
            # If "right" is already out of bounds, decrement "left"
            elif right >= n: 
                left -= 1
                
            # Otherwise
            else:
                leftDifference = abs(arr[left] - x)
                rightDifference = abs(arr[right] - x)
                
                # If the left index element has the smaller or even the same difference with "x" as right index element
                # Then decrement the left index element
                # Since it is given in the problem statement that in case of a tie, choose the smaller element
                if leftDifference <= rightDifference: 
                    left -= 1
                else: 
                    right += 1
                     
            # Decrement k
            k -= 1
        
        # Finally, we have the two boundary indices - left and right
        # And between these two, we have the "k" closest elements
        # And since array is already sorted, there is no need to sort the output again
        return arr[left+1:right]

arr = [1,2,3,4,5]
k = 4
x = 3
print("Output -> ", findClosestElements(arr,k,x))