from collections import defaultdict
def maximumSum(nums) -> int:

	# Length of the list
        n = len(nums)
        
        # Maixmum Sum value to return
        maxVal = -1
        
        # Dictionary where each value is a list
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
            # And the value is a list so we will push the "num" into the list
            # But, since we only want the two largest numbers in each group
            # We can avoid keeping more than two numbers in each group 
            
            # If the list doesn't yet has any numbers already, simply push it
            if not groups[digitSum]: groups[digitSum].append(num)
            
            # Otherwise
            else:
                # If there is only one value in the list
                if len(groups[digitSum]) == 1:
                    # If the current number is greater than the value currently in the list
                    if num > groups[digitSum][0]:
                        # Then the current number is currently the greatest for this group
                        # So, the existing value should be the second greatest
                        secondGreatest = groups[digitSum][0]
                        groups[digitSum][0] = num
                        groups[digitSum].append(secondGreatest)
                    
                    # If current number is smaller or equal to value currently in the list
                    # Then it is the second greatest so simply push it to the list
                    else: groups[digitSum].append(num)
                
                # If there are already two values in the list
                else:
                    # If current num is the greatest
                    if num >= groups[digitSum][0]:
                        prevGreatest = groups[digitSum][0]
                        groups[digitSum][0] = num
                        groups[digitSum][1] = prevGreatest
                        
                    # If current num is second greatest
                    elif num >= groups[digitSum][1]: groups[digitSum][1] = num
        
        # Now that we have our groups, we can go over each group,
        # take the sum of the two greatest numbers
        # And update the maximum value
        for key in groups:
            
            # If the group has less than 2 numbers, skip it
            if len(groups[key]) < 2: continue
                
            # Take the greatest two numbers from this group
            firstGreatest = groups[key][0]
            secondGreatest = groups[key][1]
        
            # Update the maximum sum value
            maxVal = max(maxVal, firstGreatest + secondGreatest)

        # Return the maximum value
        return maxVal


nums = [18,43,36,13,7]
print("Output -> ", maximumSum(nums))