def longestDiverseString(a: int, b: int, c: int) -> str:
	# Output to return
        output = []
        
        # We have only three values "a", "b" and "c" to work with
        # So, heap is an overkill just to keep track of the greatest
        # Let's keep track of a,b and c using a dictionary
        
        freq = {"a" : a, "b" : b, "c" : c, "z" : 0}
        
        
        # firstGreatest & second greatest
        firstGreatest = "z"
        secondGreatest = "z"
        
        
        for key in freq:
            if freq[key] > freq[firstGreatest]:
                secondGreatest = firstGreatest
                firstGreatest = key
            elif freq[key] > freq[secondGreatest]:
                secondGreatest = key
        
        # What was the previous character used
        previousCharacter = "z"
        
        # While we have at least 1 occurance to use of firstGreatest character
        while freq[firstGreatest] > 0:
            
            # 1. Previous character used is not same as the character with greatest occurances available
            if previousCharacter != firstGreatest:
                
                # We can use at most 2 occurances of this character
                occurancesUsed = min(2, freq[firstGreatest])
                
                # Push the character to output
                output.append(firstGreatest * occurancesUsed)
                
                # Update the previousCharacter
                previousCharacter = firstGreatest
                
                # Update the frequency in the dictionary
                freq[firstGreatest] -= occurancesUsed
                
            # 2. Previous character used is same as the character with the greatest occurances available
            else:
                
                # If the secondGreatest character's available occurances are already 0, break
                if freq[secondGreatest] == 0: break
                
                # We will use the secondGreatest character now but only once
                output.append(secondGreatest)
                
                # Update the previousCharacter
                previousCharacter = secondGreatest
                
                # Update the frequency in the dictionary
                freq[secondGreatest] -= 1
                
                
            # Finally, we also want to update first and second greatest values in each iteration
            # The time complexity of the below for loop is O(1) because it runs only 4 times in each iteration of outer loop
            firstGreatest = "z"
            secondGreatest = "z"
            for key in freq:
                if freq[key] > freq[firstGreatest]:
                    secondGreatest = firstGreatest
                    firstGreatest = key
                elif freq[key] > freq[secondGreatest]:
                    secondGreatest = key
                
        # Return the string
        return "".join(output)


a = 2
b = 4
c = 10

print(longestDiverseString(a,b,c))




