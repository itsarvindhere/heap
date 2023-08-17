# PROBLEM STATEMENT

Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

 - SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
 - int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
 - void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.

# EXAMPLE

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]

Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].

# APPROACH

When we reserve a seat, we want the minimum available seat number.

When we unreserve a seat, we want to put that seatnumber in our list and we want to keep the order maintained so that we have seat numbers from smallest to greatest.

And there is one data structure that can take care of ordering and will give us the smallest seat number at any time. That data structure is a "MIN HEAP".

So, we can use a Min Heap to keep track of unreserved seats and whenever we want to reserve a seat, we simply pop from the top of the MinHeap.

When we unreserve, we will push the seat number back to the heap so that it takes care of putting it in the correct place to maintain the order.