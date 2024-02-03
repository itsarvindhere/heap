from heapq import heappush, heappop
def minRefuelStops(target, startFuel, stations):
        
        # How many stops we took
        stops = 0
        
        # Number of fuel stations
        n = len(stations)
        
        # Keep track of the fuel
        # To reach the "target", we need at least "target" litres of fuel
        fuel = startFuel
        
        # A MAX Heap to keep track of the fuel stations by the amount of fuel that they have
        maxHeap = []
        
        # To keep track of the fuel stations
        i = 0
        
        # We need to travel at least "target" distance successfully
        # So, we need at least "target" litres of fuel
        while fuel < target:
            
            # Put all the fuel stations in the maxHeap that we covered
            # If we have travelled "fuel" miles so far
            while i < n and stations[i][0] <= fuel: 
                heappush(maxHeap, -stations[i][1])
                i += 1
                
            # Since fuel < target, it means we need to refuel our vehicle to increase the distance we can cover
            # For that, we will look at the fuel station on top of the maxHeap
            # Since the station on top of the maxHeap has the most fuel
            # If max Heap is empty, it means we cannot move any further so we can straight away return -1
            if not maxHeap: return -1
            
            # Update fuel by the amount of fuel that the top station has
            fuel += -heappop(maxHeap)
            
            # Update the stops
            stops += 1

        # Return the number of stops
        return stops


target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]


print("Output ->", minRefuelStops(target, startFuel, stations))