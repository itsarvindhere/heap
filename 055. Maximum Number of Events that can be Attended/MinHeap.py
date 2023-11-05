from heapq import heappop, heappush
def maxEvents(events) -> int:
        
        # Events attended
        count = 0
        
        # Minimum and maximum "day" value among all events
        start,end = 10**5,1
        
        n = len(events)
        for i in range(n):
            start = min(start, events[i][0])
            end = max(end, events[i][1])
            
        # # Sort the events by their "start" time
        events.sort()
        
        # A MinHeap to keep track of an event and its end day
        endDays = []
        
        # To keep track of events 
        i = 0
        
        # Main Logic
        for day in range(start, end + 1):
            
            # Remove all the events that have already ended
            while endDays and endDays[0] < day: heappop(endDays)
            
            # On this "day", whatever events have started, we can attend any one of them
            # It is also possible that some events are there that have started before "day"
            # But we haven't still attended them
            # So, we have to choose one event to attend on current "day" out of all those
            
            # Put the end times of all the candidates in the minHeap
            # Since the most optimal way is to choose the event that ends first out of all the candidates
            while i < n and events[i][0] == day:
                heappush(endDays, events[i][1])
                i += 1
                
            # Now, we can choose an event to atend from the top of "endDays" minHeap
            if endDays:
                heappop(endDays)
                count += 1

        # Return the maximum number of events attended
        return count

events = [[1,5],[1,5],[1,5],[2,3],[2,3]]

print("Output ->", maxEvents(events))