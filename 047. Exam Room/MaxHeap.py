from heapq import heapify, heappop, heappush
class ExamRoom:  

    def __init__(self, n: int):
        # Number of seats
        self.n = n
        
        # Max Heap
        self.maxHeap = []        

    def seat(self) -> int:
        
        # If heap is empty, then the whole row of seats is an available interval to us
        if not self.maxHeap:
            # left and right boundaries of this interval
            left,right = -1, self.n
        
        # Otherwise, we take the interval with the maximum distance between left and right boundaries
        # Note that here, boundaries simply mean at "left" and "right" indices, seats are occupied
        # And between these indices, there are available seats
        else:
            top = heappop(self.maxHeap)
            left,right = top[1], top[2]
            
            
        # Now that we have "left" and "right", let's decide at what seat person will sit
        
        # If all seats are empty, sit at the seat 0
        if left == -1: seat = 0
            
        # If a person is sitting at "left" index but there is no occupied seat on "right", 
        # Sit at right most seat, that is, n - 1
        elif right == self.n: seat = self.n - 1
            
        # If seat "left" and "right" are occupied
        # Sit at "floor of (left + right / 2)" seat
        else: seat = (left + right) // 2
            
        # Now that we know at what "seat" person will sit, two new intervals will be created
        # First is from "left" to "seat" and the other is from "seat" to "right"
        # So we push these two intervals to the Max Heap 
        # The deciding value based on which these intervals will be ordered is closest distance
        # So, for interval [left,seat] this distance is floor(seat - left / 2)
        # For the interval [seat,right] this distance is floor(right - seat / 2)
        
        # Closest Distance for the Left Interval => [left,seat]
        closestDistanceForLeftInterval = (seat - left) // 2
        
        # If "left" is -1 then the most optimal seat is seat "0"
		# And since interval is [left,seat] the closest distance will be "seat" only
        if left == -1: closestDistanceForLeftInterval = seat
        
        # Closest Distance for the Right Interval => [seat,right]
        closestDistanceForRightInterval = (right - seat) // 2
        
        # If "right" is "n" then the interval is [seat, n]
        # So, for this interval, the most optimal seat is the seat n - 1
        # So, the distance from most optimal seat to the "seat" will be "self.n - 1 - seat"
        if right == self.n: closestDistanceForRightInterval = self.n - 1 - seat

        # Push these two intervals in the maxHeap
        heappush(self.maxHeap, [-closestDistanceForLeftInterval, left, seat])
        heappush(self.maxHeap, [-closestDistanceForRightInterval, seat, right])
        
        # Return the seat number at which student will sit
        return seat
        

    def leave(self, p: int) -> None:
        
        # Now, just imagine what happens when a person leaves a seat
        # For example, if at any point, we have three person sitting in a row of 10 seats
        # Then seats "0", "4" and "9" will be occupied
        # And if person "4" leaves, it means, 
		# we should now remove the intervals from maxHeap which either start with "4" or end with "4"
        # Because those intervals are no longer valid now that the seat "4" itself is empty
        
        intervalStartsAtP = None
        intervalEndsAtP = None
        
        # Let's just loop over the maxHeap since it is just a list internally
        for interval in self.maxHeap:
            # If this interval starts with "p"
            # This should be removed
            if interval[1] == p: intervalStartsAtP = interval
            
            # If this interval ends with "p"
            # This should be removed
            if interval[2] == p: intervalEndsAtP = interval
                
        # Remove the two
        self.maxHeap.remove(intervalStartsAtP)
        self.maxHeap.remove(intervalEndsAtP)
                
        # And now, the order is not proper so we have to manually call heapify here
        heapify(self.maxHeap)
        
        # Finally, since we remove the two intervals, it means a bigger interval is now available to us
        # Imagine that the two intervals we removed are [left, p] and [p, right]
        # So, it means [left,right] is now a new larger interval available to us, right?
        # So, put it in the heap
        left = intervalEndsAtP[1]
        right = intervalStartsAtP[2]
        
        # The same logic to get the closest distance as in seat() method
        closestDistance = (right - left) // 2
        
        # If "left" is -1 then the most optimal option is seat "0"
        # It means, if next person sits at seat "0", the closest seat will be at "right"
        # So closest distance here is "right"
        if left == -1: closestDistance = right
            
        # If "right" is "n" then the interval is [left, n]
        # So, for this interval, the most optimal seat is the seat n - 1
        # So, the distance from most optimal seat to the "left" will be "self.n - 1 - left"
        elif right == self.n: closestDistance = self.n - 1 - left
        
        # Push this interval in the maxHeap with its closest distance value
        heappush(self.maxHeap, [-closestDistance, left, right])