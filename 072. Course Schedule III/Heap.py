from heapq import heappush, heappop
def scheduleCourse(courses) -> int:
        # Sort the courses by the "lastDay"
        # Why "lastDay"?
        # Because if "i" course ends on day "x", 
        # we can be sure that the "i + 1" course will end at or after "x"
        # So the basic idea is to try to complete the courses that are ending first
        courses.sort(key = lambda x: x[1])
        
        # A Max Heap to keep track of the courses taken so far
        maxHeap = []
        
        # To keep track of the currentDay
        currentDay = 0
        
        for duration,lastDay in courses:
            
            # At what day you will finish the current course if you take it today?
            finishDay = currentDay + duration
            
            # If you can finish it before or at the "lastDay" then take the course
            if finishDay <= lastDay:
                
                # Update the currentDay to the day when you will finish the current course
                currentDay += duration
                
                # Push the course to the maxHeap
                heappush(maxHeap, -duration)
                
            # If you cannot finish it by "lastDay"
            elif maxHeap:
                
                # So far, we have spend "currentDay" number of days taking courses
                # And at this point, for the current course, 
                # we do not have enough days left to finish it before deadline
                
                # So, we can remove one course that we took already
                # And in place of that course, we can take the current course
                # But, the only reason to do this would be if taking the current course reduces the "currentDay" value
                # That is, if we had taken the current course instead of course "x", 
                # then we would've completed same number of courses so far but in lesser days
                
                # So, which course should be removed that we have already taken?
                # Well, that would be the one that took the longest to complete
                # Because if in place of that course, we take the current course
                # Then it might reduce the overall "currentDay" value
                # And only if it does, then it makes sense to replace that course with the current course
                # And that's why, the maxHeap is used in this solution to quickly access the course taken so far with longest duration
                
                # The course on top of the maxHeap has the longest duration
                topDuration = -maxHeap[0]
                
                # If we undo the course on top of the maxHeap, how many days will get reduced
                # That would be "currentDay - topDuration"
                # So, if instead of the course on top of the maxHeap, we had taken the current course instead
                # Then what would've been the value of the currentDay
                # That would've been (currentDay - topDuration) + duration
                newDayAfterDoingCurrentCourse = (currentDay - topDuration) + duration
                
                # So, if this value is smaller than "currentyDay"
                # Then it means it makes more sense to take the current course instead of course on top of the maxHeap
                # Because since the "currentDay" value has been reduced
                # It means, we now have extra days with us than before, and so, chances of completing more courses have increased
                if newDayAfterDoingCurrentCourse < currentDay:
                    heappop(maxHeap)
                    currentDay -= topDuration
                    currentDay += duration
                    heappush(maxHeap, -duration)
                    
        # Finally, the number of entries in the maxHeap = Maximum number of courses we can take
        return len(maxHeap)

courses = [[1, 12], [6, 15], [10, 12], [3, 20], [10, 19]]

print("Output ->", scheduleCourse(courses))