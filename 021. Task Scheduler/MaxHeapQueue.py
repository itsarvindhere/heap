from collections import Counter, deque
from heapq import heappop, heappush


def leastInterval(tasks, n: int) -> int:
        
        # Time taken by the CPU to complete all the tasks
        timeTaken = 0
        
        # Keep track of how many times each task appear in the tasks list
        freq = Counter(tasks)
        
        # The most optimal way is to try to do the most frequent tasks first
        # So at any time, we want to have the tasks ordered by their frequency from most to least
        # And so, we can use a maxHeap here for that
        
        # Our max heap will have all the frequency values in it
        maxHeap = []
        for val in freq.values(): heappush(maxHeap, -val)
            
        # Queue to keep the frequency values we already computed from heap
        # So that we can put them back in heap when we can use them
        # Basically, we will keep the tasks in this queue that we cannot yet execute
        queue = deque()
        
        # While we have tasks to execute
        while maxHeap or queue:
            
            # If we have task to execute then it will take 1 unit of time
            # If we don't, then also 1 unit of time will be spent for being idle
            timeTaken += 1
            
            # Now we can pop the task from top of heap and put it in the queue
            # Since we cannot use it at till we are at (timeTaken + n) time
            # So, we will push a pair to the queue -> (task freq, time when we can use it again)
            # But, we will only put it in the queue if we know that there are more such tasks yet to be executed
            if maxHeap:
                
                # Frequency of task on top of heap
                freqOfTopTask = -heappop(maxHeap)
                
                # Reduce frequency of this task by 1 since we executed it once
                freqOfTopTask -= 1
                
                # If frequency is not 0, we put it in the queue with the time at which we can use it again
                if freqOfTopTask != 0: queue.append((freqOfTopTask, timeTaken + n))
        
            # If at the front of queue, we have a task we can use at current "timeTaken" time
            # We will push it back to the heap
            if queue and queue[0][1] == timeTaken: heappush(maxHeap, -queue.popleft()[0])

        
        # Return the minimum time taken
        return timeTaken

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2

print("Output -> ", leastInterval(tasks,n))