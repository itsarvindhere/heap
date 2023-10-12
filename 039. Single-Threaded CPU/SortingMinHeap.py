from heapq import heappop, heappush


def getOrder(tasks):
        
        # Output List
        output = []
        
        # Length of the list
        n = len(tasks)
        
        # First, we will sort the tasks by their enqueue time
        # Also, since we want to keep track of the original indices
        # We will convert each task into a triplet where we also have the original indx
        tasks = [[tasks[i][0], tasks[i][1], i] for i in range(n)]
        
        # Sort the tasks
        tasks.sort()
        
        # minHeap to keep track of the available tasks that CPU can choose from
        # This minHeap will order the tasks by their "processing time"
        availableTasks = []
        
        # The time at which CPU is available to process a task
        # Initially, it will be available to process a task at the enqueue time of first task (since tasks are sorted)
        time = tasks[0][0]
        
        # Pointer to keep track of tasks
        i = 0
        
        while i < n or availableTasks:
            
            # Whatever tasks have enqueue time <= "time", put them in availableTasks heap
            while i < n and tasks[i][0] <= time:
                # The available tasks will be orderd by processing time
                heappush(availableTasks, [tasks[i][1], tasks[i][2], tasks[i][0]])
                
                # Increment i
                i += 1
            
            # If there are available tasks to process
            if availableTasks:

                # The CPU will take the task that has the shortest processing time
                currentTask = heappop(availableTasks)

                # Put the index in output
                output.append(currentTask[1])

                # And now, the CPU will be available to process another task after "time + currentTask[1]" time
                time += currentTask[0]
            
            # If there is no "available" task, then CPU will remain idle 
            # until it picks up the next task with the least enqueue time
            # So, instead of waiting, just update the time to the next smallest enqueue time from the tasks
            else: time = tasks[i][0]
            
		# Finally, return the output list
        return output


tasks = [[1,2],[2,4],[3,2],[4,1]]

print("Output ->", getOrder(tasks))