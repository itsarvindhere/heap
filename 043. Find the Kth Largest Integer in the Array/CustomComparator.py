from functools import cmp_to_key
# Custom Compare method
# A comparison function is any callable that accepts two arguments, 
# compares them, and returns a negative number for less-than, 
# zero for equality, or a positive number for greater-than. 
def comparator(first, second):
        
    # If the length of "first" is greater than "second"
    # Then first is greater than second
    if len(first) > len(second): return 1
        
    # If the length of "first" is less than "second"
    # Then "first" is smaller than "second"
    elif len(first) < len(second): return -1
        
    # If both have the same lengths, compare their individual characters/digits
    else:
            
        # Pointers for each
        i,j = 0,0
            
        # Length of both
        n = len(first)
            
        # Go over individual digits
        while i < n and j < n:
                
            # If the "i" digit of "first" is greater than "j" digit of "second"
            # Then "first" is greater than "second"
            if first[i] > second[j]: return 1

            # If the "i" digit of "first" is smaller than "j" digit of "second"
            # Then "first" is smaller than "second"
            elif first[i] < second[j]: return -1
                
            # If both have same digits, move on to next comparison
            else: 
                i += 1
                j += 1
                    
    # Finally, if nothing is returned so far, then both are equal
    return 0
        
def kthLargestNumber(nums, k: int) -> str:
        
    # Sort the list based on the custom comparator
    # In Python 3, the cmp parameter has been removed
    # But we can use the functools.cmp_to_key(func) 
    # To comvert "cmp" to "key"
    # So, that's what we will use here
    nums.sort(key=cmp_to_key(comparator), reverse = True)
        
    # And finally, return the kth largest value
    return nums[k - 1]

nums = ["2","21","12","1"]
k = 3

print("Output -> ", kthLargestNumber(nums,k))