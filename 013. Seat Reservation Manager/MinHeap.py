from heapq import heappop, heappush


class SeatManager:

    def __init__(self, n: int):
        
        # A min heap that gives us the smallest available unreserved seat
        self.minHeap = [i for i in range(1,n + 1)]

    def reserve(self) -> int:
        
        # When we want to reserve a seat, we reserve the smallest numbered seat
        # So, pop from top of minHeap
        return heappop(self.minHeap)

    def unreserve(self, seatNumber: int) -> None:
        
        # When we unreserve a set, we push that seat number back into the heap
        heappush(self.minHeap, seatNumber)

