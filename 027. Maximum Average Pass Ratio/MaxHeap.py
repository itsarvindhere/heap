from heapq import heappop, heappush
def maxAverageRatio(classes, extraStudents: int) -> float:

		# Number of classes
        n = len(classes)
        
        # MaxHeap
        maxHeap = []
        
        for i in range(n):
            # What would be the increase in pass ratio if a student is assigned to this class?
            # It would be newPassRatio - oldPassRatio
            oldPassRatio = classes[i][0] / classes[i][1]
            newPassRatio = (classes[i][0] + 1) / (classes[i][1] + 1)
            
            increaseInPassRatio = newPassRatio - oldPassRatio
            
            # We want to order classes by their increaseInPassRatio
            # That's why increaseInPassRatio is the first item
            # It is in negative so that we can utilize the minHeap in python as a maxHeap
            heappush(maxHeap, [-increaseInPassRatio, classes[i]])
            
        # Now, we can start assigning classes
        while extraStudents > 0:
            
            # Take the classes with highest increaseInPassRatio if we assign a student to it
            top = heappop(maxHeap)
            
            # Assign the student to this class
            extraStudents -= 1
            
            top[1][0] += 1
            top[1][1] += 1
            
            # Now, before we push it back to the maxHeap
            # We want to calculate the new "increaseInPassRatio" value since we added one student to it
            oldPassRatio = top[1][0] / top[1][1]
            newPassRatio = (top[1][0] + 1) / (top[1][1] + 1)
            
            increaseInPassRatio = newPassRatio - oldPassRatio
            
            top[0] = -increaseInPassRatio
            
            # Now, we can push back this data in the maxHeap
            heappush(maxHeap, top)
        
        # Now, we will calculate the total of pass ratios of all the classes
        totalPassRatio = 0
        while maxHeap:
            top = heappop(maxHeap)
            
            totalPassRatio += top[1][0] / top[1][1]
        
        # And finally, return the Average Pass Ratio
        return totalPassRatio / n


classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4

print("Output -> ", maxAverageRatio(classes, extraStudents))