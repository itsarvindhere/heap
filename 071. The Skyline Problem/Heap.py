from heapq import heappush,heappop
def getSkyline(buildings):
        
        # How many buildings are there
        n = len(buildings)
        
        # A Max heap for Height Values to keep track of the buildings with the maximum height
        heightValues = []
        
        # Output list to return
        output = []
        
        # Each point on the X-axis
        xValues = []
        for i in range(n):
            # Here, "True" means it is the left edge/start of a building
            xValues.append([buildings[i][0], buildings[i][2],True])
            xValues.append([buildings[i][1], buildings[i][2], False])
        
        # Sort the points
        xValues.sort()
        
        # Removed height values and their count
        # Using this, we can delete values from top of the heap when required
        # instead of deleting from between the heap which is not efficienct
        removedValues = {}
        
        # Go over the points across the x axis from left to right
        for i in range(len(xValues)):
            
            xVal,height,isLeftEdge = xValues[i]
            
            # Current maximum height
            maxHeight = 0 if not heightValues else -heightValues[0]
            
            # If this is the left edge of the building, push its height to the maxHeap
            if isLeftEdge: heappush(heightValues, -height)
                
            # If this is the right edge of the building, its height needs to be removed from the maxHeap
            # But, we won't remove it from the heap directly because it is not necessary that
            # the value to be removed is on top of the maxHeap
            # So, we instead push all the deleted values with their counts in a dictionary
            else: removedValues[height] = removedValues.get(height,0) + 1
            
            # Remove the stale values from maxHeap
            # That is, all the values in the dictionary
            while heightValues:
                h = -heightValues[0]
                if h in removedValues and removedValues[h] > 0: 
                    removedValues[h] -= 1
                    heappop(heightValues)
                else: break
            
            # If at the same point one building ends and another starts
            # Skip
            if i + 1 < len(xValues) and xValues[i][0] == xValues[i + 1][0]: continue
        
            # Value to add to the output list
            val = []
            
            # If there are no height values in the heap
            if not heightValues: val = [xVal, 0]
            
            # If the maximum height is same as the height of current building
            # This is the tallent building so far
            # So, simply push (xVal,height) in the output list
            elif -heightValues[0] == height: val = [xVal,height]
            
            # If this is the end/right edge of the building and the height value in max heap changed
            # It means this building was the highest so far but it is no longer the highest
            # So, in the output list, the pair to push will be (xVal, height on top of the maxHeap)
            # This is the same scenario as in Example 1 when red building ends at "7" on x-axis
            # And so, the new highest building at that point is green building with height 12
            # Hence, we push (7,12) in the output list
            elif not isLeftEdge and -heightValues[0] != maxHeight: val = [xVal, -heightValues[0]]
            
            # Push the val to the output list only if the previous value in output list doesn't have same height
            if val and (not output or output[-1][1] != val[1]): output.append(val)
        
        # Return the output list
        return output

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

print("Output ->", getSkyline(buildings))