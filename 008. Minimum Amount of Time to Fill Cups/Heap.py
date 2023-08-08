from heapq import heappop, heappush


def fillCups(amount) -> int:
        # Minimum seconds needed
        minimumSeconds = 0
        
        # Going through the examples, we can see that the most optimal approach is
        # To take the two greatest values each second (if we have two values > 0)
        # And reduce both by 1
        
        # Instead of sorting in each iteration
        # We can use a maxHeap here
        # Because a maxHeap will always give us the two largest elements at any time automatically
        maxHeap = []
        for val in amount: 
            if val != 0: heappush(maxHeap, -val)
                
                
        # If there is no non-zero value (all values are 0)
        if not maxHeap: return minimumSeconds
        
        # If there is only one non zero value then we would require same number of seconds as that value itself
        if len(maxHeap) == 1: return -maxHeap[0]
            
        
        # While all values are not zero, keep doing the operations each second
        while -maxHeap[0] > 0:
            
            # Take the first and second greatest values and if both are > 0, we can fill two cups in one second
            # If both first and second greatest are not > 0, then it means we can only fill one cup in a second
            if -maxHeap[0] > 0 or -maxHeap[1] > 0:
                if -maxHeap[0] > 0 and -maxHeap[1] > 0:
                    firstGreatest = -heappop(maxHeap)
                    secondGreatest = -heappop(maxHeap)
                    heappush(maxHeap, -(firstGreatest - 1))
                    heappush(maxHeap, -(secondGreatest - 1))
                    
                # If only one of them is > 0, then it is obviously the greater value among the two
                # That is, the first greatest
                else: 
                    firstGreatest = -heappop(maxHeap)
                    heappush(maxHeap, -(firstGreatest - 1))
                
                # Increment the seconds
                minimumSeconds += 1            

        
        return minimumSeconds


amount = [5,4,4]
print("Output ->",fillCups(amount))