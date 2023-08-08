def fillCups(amount) -> int:
        # Minimum seconds needed
        minimumSeconds = 0
        
        # Going through the examples, we can see that the most optimal approach is
        # To take the two greatest values each second (if we have two values > 0)
        # And reduce both by 1
        
        # Let's sort the list to get the two greatest
        amount.sort()
                        
        # While all values are not zero, keep doing the operations each second
        while amount[-1] > 0:
            
            
            # Take the first and second greatest values and if both are > 0, we can fill two cups in one second
            # If both first and second greatest are not > 0, then it means we can only fill one cup in a second
            if amount[-1] > 0 or amount[-2] > 0:
                if amount[-1] > 0 and amount[-2] > 0:
                    amount[-1] -= 1
                    amount[-2] -= 1
                    
                # If only one of them is > 0, then it is obviously the greater value among the two
                # That is, the first greatest
                else: amount[-1] -= 1
                
                # Increment the seconds
                minimumSeconds += 1            

            # Now, we again need to do the same process to get the new first and second greatest elements
            # So, let's sort again
            amount.sort()
        
        return minimumSeconds


amount = [5,4,4]
print("Output ->",fillCups(amount))