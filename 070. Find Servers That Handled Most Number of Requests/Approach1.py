from heapq import heappush, heappop
def busiestServers(k: int, arrival, load):
        
        # How many requests are there
        n = len(arrival)
        
        # Initially all the servers are available
        # So, we will put all the available servers a queue-like data structure
        # This will order the servers by their indices from smallest to largest
        # So, it will be a MIN HEAP
        availableServers = []  
        
        # A Set to keep track of the server indices of available servers
        # So that we can quickly check if i%k server is available or not
        availableSet = set()
        
        # Initially, all servers are available
        for i in range(k): 
            heappush(availableServers, i)
            availableSet.add(i)
        
        # Another queue-like data structure that will be used to keep track of all the busy servers
        # This will order the servers by the time at which they will be available again (from smallest to largest)
        # So, it will be a MIN HEAP
        busyServers = []
        
        # A dictionary to keep track of how many requests each server handled
        requestCount = {}
        
        # We will go over the arrival times from left to right
        for i in range(n):
            
            # First, check if there are servers in the "busyServers"  Min Heap
            # That should be available by the current arrival time
            # If yes, then move them back to the available servers list
            while busyServers and busyServers[0][0] <= arrival[i]: 
                
                # Index of the server on top of "busyServers" Min Heap
                idx = heappop(busyServers)[1]
                
                # Add the server back to the "availableServers"
                heappush(availableServers, idx)
                
                # Also add the server to the availableServers set
                availableSet.add(idx)
                
                
            # If the servers on top of the "availableServers" minHeap are not in "availableSet"
            # Remove them from the minHeap
            while availableServers and availableServers[0] not in availableSet: heappop(availableServers)
                
            # If no servers are available, skip current request
            if not availableSet: continue
                
            reqServer = i % k
            while reqServer < k and reqServer not in availableSet: reqServer += 1
            
            if reqServer in availableSet:
                heappush(busyServers, [arrival[i] + load[i], reqServer])
                availableSet.remove(reqServer)
                requestCount[reqServer] = requestCount.get(reqServer,0) + 1
            else:
                idx = heappop(availableServers)
                heappush(busyServers, [arrival[i] + load[i], idx])
                availableSet.remove(idx)
                requestCount[idx] = requestCount.get(idx,0) + 1
                

        # What is the maximum count of requests handled
        maxCount = max(requestCount.values())

        # Return all the servers that handles "maxCount" number of requests     
        return [key for key in requestCount if requestCount[key] == maxCount]


k = 3
arrival = [1,2,3,4,5]
load = [5,2,3,3,3]
print("Output ->", busiestServers(k, arrival ,load))