from heapq import heappop, heappush
def totalCost(costs, k: int, candidates: int) -> int:
    # Total cost to return
    cost = 0
        
    # Length of the list
    n = len(costs)
        
    # left candidates
    leftCandidates = []
        
    # right candidates
    rightCandidates = []
        
    # First, we will fill the two minHeaps with data of "candidates" workers
    # leftCandidates will have data of "candidates" workers from the beginning
    # rightCandidates will have data of "candidates" workers from the end
    for i in range(n):
        if i < candidates: heappush(leftCandidates, costs[i])
        elif i >= n - candidates: heappush(rightCandidates, costs[i])
                
                
    # Two pointers to track the remaining workers that are not part of left or right candidates
    i,j = candidates, n - candidates - 1
        
    # Now we start with the logic
    # We want to hire "k" workers
    while k > 0:
            
        # We want the lowest value among the two parts - "leftCandidates" and "rightCandidates"
            
            
        # If the "rightCandidates" are empty
        # OR
        # If lowest cost in "leftCandidates" is smaller or equal than lowest cost in "rightCandidates" 
        # We will choose the worker from "leftCandidates"
        if not rightCandidates or (leftCandidates and rightCandidates and leftCandidates[0] <= rightCandidates[0]):
            # Increment the cost
            cost += heappop(leftCandidates)
                
            # Since we removed one, add one candidate into leftCandidates based on "i" and "j" pointers
            # Note that since we are adding into leftCandidates, we will add from left side
            if i <= j: 
                heappush(leftCandidates, costs[i])
                i += 1
                    
            
        # If the "leftCandidates" are empty
        # OR
        # If lowest cost in "leftCandidates" is greater than lowest cost in "rightCandidates" 
        # We will choose the worker from "rightCandidates"
        elif not leftCandidates or (leftCandidates and leftCandidates and leftCandidates[0] > rightCandidates[0]):
            # Increment the cost
            cost += heappop(rightCandidates)
                
            # Since we removed one, add one candidate into "rightCandidates" based on "i" and "j" pointers
            # Note that since we are adding into "rightCandidates", we will add from right side
            if j >= i: 
                heappush(rightCandidates, costs[j])
                j -= 1
                    
        # Decrement k
        k -= 1
        
    # Finally, return the total cost for hiring k workers
    return cost


costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

print("Output -> ", totalCost(costs,k, candidates))