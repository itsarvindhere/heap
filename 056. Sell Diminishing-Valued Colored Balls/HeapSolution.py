from heapq import heappop, heappush


def maxProfit(inventory, orders: int) -> int:

	# Profit
	profit = 0

	# Max Heap
	maxHeap = []

	for val in inventory: heappush(maxHeap, -val)

	while orders > 0:

		# Get the highest value from top of maxHeap
		top = -heappop(maxHeap)

		# Increment profit
		profit += top

		# Put the (value - 1) back 
		heappush(maxHeap, -(top - 1))

		# Decrement orders
		orders -= 1

	return profit

inventory = [4,2,7,1]
orders = 6

print("Output ->", maxProfit(inventory, orders))