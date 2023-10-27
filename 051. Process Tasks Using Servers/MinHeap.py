from heapq import heappop, heappush
def assignTasks(servers, tasks):
        
    # Lengths
    m,n = len(servers), len(tasks)
        
    # Output list of same length as "tasks"
    output = [-1] * n
        
    # The servers are selected based on their weight
    # And if weight is same for two servers, we select the one with a smaller index
    # So, to keep track of this data, we can use a minHeap
    freeServers = []
        
    # Note that we are pushing a triplet in minHeap
    # The reason being that if two servers have same weight
    # Then minHeap will use the "index" or the "second value in triplet" to break the tie
    for i in range(m): heappush(freeServers, [servers[i],i,i])
        
    # Another min Heap that we will use to keep all the servers that are currently processing tasks 
    # These will be orderd by the time at which they become free again so that we can put then back in "freeServers"
    busyServers = []
        
    # To keep track of time at which a task can be processed
    # All the tasks with index <= time
    # are eligible to be processed at the same time by multiple servers (if available)
    time = 0
        
    # Loop over the tasks
    i = 0
    while i < n:
            
        # If there are no free servers
        if not freeServers:
            # Update the "time" to the earliest time at which a task can be processed
            # Because at that time, at least one server will become free again
            time = busyServers[0][0]

        time = max(time,i)
                
        # Now, at "time" seconds, all the servers that become free should be put back in "freeServers"
        while busyServers and busyServers[0][0] <= time:
            top = heappop(busyServers)
            heappush(freeServers, [top[1], top[2], top[2]])
                
        # And now, we can process all the tasks that are available at current "time"
        while i < n and i <= time and freeServers:
            # Get the available server with the smallest weight (or index,if a tie)
            top = heappop(freeServers)
                
            # When will be become free again?
            availableTime = time + tasks[i]
                
            # Put it in the busyServers heap
            heappush(busyServers, [availableTime, top[0], top[1]])
                
            # Update the output list
            output[i] = top[1]
                
            # Increment i
            i += 1

    # Finally, return the output list
    return output

servers = [3,3,2]
tasks = [1,2,3,2,1,2]

print("Output -> ", assignTasks(servers,tasks))