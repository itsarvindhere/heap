from heapq import heappush, heappop
def findMaximizedCapital(k: int, w: int, profits, capital) -> int:

	# Finished projects
	finishedProjects = set()

	# Number of projects
	n = len(profits)

	while len(finishedProjects) < k:

		# Find the project, from the projects that we can take,
		# that will give us the maximum profit
		maxProfitProject = -1
		maxProfit = -1

		for i in range(n):
			if i not in finishedProjects and capital[i] <= w and profits[i] > maxProfit:
				maxProfit = profits[i]
				maxProfitProject = i

		# If no project can be taken, break
		if maxProfitProject == -1: break

		# Add the project to the set
		finishedProjects.add(maxProfitProject)

		# Update the capital
		w += maxProfit

	# Return the final maximized capital
	return w

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]

print("Output is ->", findMaximizedCapital(k, w, profits, capital))