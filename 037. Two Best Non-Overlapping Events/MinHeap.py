from heapq import heappop, heappush

def maxTwoEvents(events) -> int:
        
        # Maximum Sum
        maxSum = 0
        
        # Length of the list
        n = len(events)
        
        # A Brute Force solution will fail
        # Because, for every event, we have to loop over the whole list
        # When it comes to intervals and sorting related problems, sorting is something we can use
        # because sorting makes checking for overlaps easier
        
        # Let's sort the events by their start values
        events.sort()
        
        # We want to quickly check for overlaps
        # So, let's have a minHeap that keeps track of events so far from least end time to maximum
        # Why minHeap? because, if an event overlaps with event on top of minHeap
        # Ofcourse it will also overlap with all other events so far since they have end value
        # greater or equal to what top of heap has 
        minHeap = []
        
        # What is the maximum "value" of an event so far before the current event that is not overlapping
        maxValueSoFar = 0
        
        # Loop over the events
        for event in events:
            
            # Our minHeap keeps the events by their "end" time from minimum to maximum
            # So, the top of minHeap at any time has the event with the smallest end time so far
            # So, if the current event overlaps that smallest end time event, ofcourse it will overlap with all events so far
            # So in this way, we don't need to compare with all the events that occured so far
            # Similarly, if the current event does not overlap with the top event
            # Then we can say all the events after it also don't overlap since events are sorted by start values
            while minHeap and event[0] > minHeap[0][0]: maxValueSoFar = max(maxValueSoFar, heappop(minHeap)[1])
            
            # Once we get the maximum possible "value" so far, we can update our maximum sum for the current "event"
            # And note that this "maxValueSoFar" will remain a possible max value for all upcoming events
            # Because as mentioned above, the list is sorted by "start" value
            # It means, if for an event "i", we have a "maxValueSoFar", 
            # Then that will also be valid for any event at index greater than "i"
            maxSum = max(maxSum, event[2] + maxValueSoFar)
            
            # Push the current event to the minHeap as well
            heappush(minHeap, (event[1], event[2]))

        # Return the maximum sum
        return maxSum


events = [[1,5,3],[1,5,1],[6,6,5]]

print("Output -> ", maxTwoEvents(events))