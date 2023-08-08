def fillCups(amount) -> int:
        # How many values are zero in amount list
        zeroCount = 0
        
        # Minimum seconds needed
        minimumSeconds = 0
        
        # Going through the examples, we can see that the most optimal approach is
        # To take the two greatest values each second (if we have two values > 0)
        # And reduce both by 1
        
        firstGreatest, secondGreatest = -1,-1
        firstGreatestIdx, secondGreatestIdx = -1, -1
        
        # Get the first and second greatest values from the list
        for i in range(3):
            value = amount[i]
            
            # If there is a zero value
            if value == 0: zeroCount += 1
                
            if value > firstGreatest:
                secondGreatest = firstGreatest
                secondGreatestIdx = firstGreatestIdx
                firstGreatest = value
                firstGreatestIdx = i
            elif value > secondGreatest:
                secondGreatest = value
                secondGreatestIdx = i
                        
        # While all values are not zero, keep doing the operations each second
        while zeroCount < 3:
            
            
            # Take the first and second greatest values and if both are > 0, we can fill two cups in one second
            if firstGreatest > 0 and secondGreatest > 0:
                amount[firstGreatestIdx] -= 1
                amount[secondGreatestIdx] -= 1
                
                if amount[firstGreatestIdx] == 0: zeroCount += 1
                if amount[secondGreatestIdx] == 0: zeroCount += 1
                    
                minimumSeconds += 1
                
            # If both first and second greatest are not > 0, then it means we can only fill one cup in a second
            elif firstGreatest > 0:
                amount[firstGreatestIdx] -= 1
                if amount[firstGreatestIdx] == 0: zeroCount += 1
                    
                minimumSeconds += 1
                
            # Now, we again need to do the same process to get the new first and second greatest elements
            firstGreatest, secondGreatest = -1,-1
            firstGreatestIdx, secondGreatestIdx = -1, -1
            for i in range(3):
                value = amount[i]

                if value > firstGreatest:
                    secondGreatest = firstGreatest
                    secondGreatestIdx = firstGreatestIdx
                    firstGreatest = value
                    firstGreatestIdx = i
                elif value > secondGreatest:
                    secondGreatest = value
                    secondGreatestIdx = i
        
        return minimumSeconds


amount = [5,4,4]
print("Output ->",fillCups(amount))