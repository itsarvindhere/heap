from heapq import heappop, heappush


def carPooling(trips, capacity: int) -> bool:
        # How many trips
        n = len(trips)
        
        # Sort the trips by their "from" values
        # Because if you draw the trips on a number line
        # You will see that since our car only moves from left to right
        # It will pick those passengers first which have a smaller "from" value
        # So that's why we will sort based on the "start" value
        trips.sort(key = lambda x: x[1])
        
        # We also want a way to figure out when to drop off the passengers and increase the capacity
        # So, we want to keep track of all the "to" values in smallest to greatest order at any time
        # For that, we can use a minHeap
        minHeap = []
        
        # Start from second trip
        for i in range(n):
            
            trip = trips[i]
            
            # If there are trips in minHeap that have already ended, update capacity accordingly
            while minHeap and minHeap[0][0] <= trip[1]: capacity += heappop(minHeap)[1]
                
            # If we have the capacity to include passengers in current trip?
            if capacity >= trip[0]:
                
                # Reudce the capacity
                capacity -= trip[0]
                
                # Put this trip in the heap
                heappush(minHeap, (trip[2], trip[0]))
                
            # Otherwise, return False
            else: return False

        # All passengers can be picked up and dropped off for all the trips
        return True

trips = [[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]]
n = 28

print("Output -> ", carPooling(trips, n))