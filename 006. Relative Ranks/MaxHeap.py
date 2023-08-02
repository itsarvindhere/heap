from heapq import heapify, heappop


def findRelativeRanks(score):
         # Length of the list
        n = len(score)
        
        # MaxHeap
        maxHeap = [(-score[i], i) for i in range(n)]
        heapify(maxHeap)
        
        # Populate correct ranks
        for i in range(n):
            
            # Index on top of the heap
            idx = heappop(maxHeap)[1]
            
            if i == 0:
                score[idx] = "Gold Medal"
            elif i == 1:
                score[idx] = "Silver Medal"
            elif i == 2:
                score[idx] = "Bronze Medal"
            else:
                score[idx] = str(i + 1)
                
        # Return the required output list
        return score


score = [10,3,8,9,4]
print("Output ->", findRelativeRanks(score))