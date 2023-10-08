from collections import Counter
def rearrangeBarcodes(barcodes):

	# Length of the list
    n = len(barcodes)
        
    # Frequency of each barcode
    count = Counter(barcodes)
            
    # For an "n" length list, a barcode can occur at least 1 time and at most n times
    freqList = [[] for i in range(n)]
        
    for key in count: freqList[count[key] - 1].append(key)

    # Since this "freqList" list is already sorted in increasing order, 
    # now we can easily keep track of first and second most occuring barcodes
        
    # i => first greatest, j => second greatest
    i,j = n - 1, n - 1
        
    # Output list
    output = []
        
    # Main Logic
    while len(output) < n:
            
        # Skip all the empty lists
        while not freqList[i]: i -= 1
                
        # If the length of "i" list is > 1, then "j" will also point to the same
        if len(freqList[i]) > 1: j = i
                
        # Otherwise, get the correct index for "j"
        else:
            while not freqList[j] or (i == j): j -= 1
                    
        # Get the most occuring barcode value
        firstGreatest = freqList[i].pop()
            
        # If the previous value in output is not same as firstGreatest
        if not output or output[-1] != firstGreatest:
            # Put this value in the output
            output.append(firstGreatest)
                
            # Since we used it once, it will now be pushed to freqList[i-1]
            # If i - 1 is not out of bounds, ofcourse
            if i > 0: freqList[i - 1].append(firstGreatest)
                    
        # If the previous value in output is the same as firstGreatest
        else:
            # Get the second greatest value
            secondGreatest = freqList[j].pop()
                
            # Now do the same as above
            # Put this value in the output
            output.append(secondGreatest)
                
            # Since we used it once, it will now be pushed to freqList[j - 1]
            # If j - 1 is not out of bounds, ofcourse
            if j > 0: freqList[j - 1].append(secondGreatest)
                    
            # And don't forget to also put back the firstGreatest to its initial place since we did not use it
            freqList[i].append(firstGreatest)
        
    # And finally, return the output list
    return output


barcodes = [1,1,1,1,2,2,3,3]

print("Output -> ", rearrangeBarcodes(barcodes))