from collections import defaultdict
from heapq import heappop, heappush
def maximumSum(nums) -> int:

	# Length of the list
        n = len(nums)
        
        # Maixmum Sum value to return
        maxVal = -1
        
        # Dictionary where each value is a minHeap
        groups = defaultdict(list)
        
        # Since we want the maximum 2 numbers having same sum of digits
        # What we can do is group numbers based on their digit sum
        
        # So, if we have lets say nums = [18,43,36,13,7]
        # Here, 18 and 36 have sum = 9 so we can put them both in a single group
        # Similarly, we can put 43 and 7 in the same group
        
        # Go we go over each element
        for num in nums:
            
            # Get the sum of its digits
            digitSum = 0
            temp = num
            while temp > 0:
                remainder = temp % 10
                digitSum += remainder
                temp //= 10
                
            # Now, this "digitSum" is a key in the dictionary
            # And the value is a minHeap so we will push the "num" into the minHeap
            heappush(groups[digitSum], num)
            
            # # We want only the two greatest numbers for each group
            # # So we can limit the minHeap size to 2
            if len(groups[digitSum]) > 2: heappop(groups[digitSum])
                
        
        # Now that we have our groups, we can go over each group,
        # take the sum of the two greatest numbers
        # And update the maximum value
        for key in groups:
            
            # If the group has less than 2 numbers, skip it
            if len(groups[key]) < 2: continue
                
            # Take the greatest two numbers from this group
            firstGreatest = heappop(groups[key])
            secondGreatest = heappop(groups[key])
            
            # Update the maximum sum value
            maxVal = max(maxVal, firstGreatest + secondGreatest)

        # Return the maximum value
        return maxVal


nums = [18,43,36,13,7]
print("Output -> ", maximumSum(nums))