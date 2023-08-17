def maximumScore(a: int, b: int, c: int) -> int:
        
        # Maximum Score
        score = 0
        
        # Since we have only three values, we can easily keep track of the first and second greatest value
        # Without having to use a heap
        
        # Let's order the values such that 
        # "a" always has the greatest value
        # "b" always has the second greatest value
        # "c" always has the third greatest value
        
        # If a is smaller than b, then swap the two values
        if a < b: a,b = b,a
            
        # If a is still smaller than c, then swap the two values
        if a < c: a,c = c,a
            
        # At this point "a" has the greatest value among the three
        # So, now we want "b" to have the second greatest value
        # We will finally check if "b" is smaller than "c"
        # If yes, then swap the two values
        if b < c: b,c = c,b
        
        # We will run our loop till the second greatest value is > 0
        while b > 0:
            
            # Decrement the values
            
            # OPTIMIZATION
            
            # Instead of us decrementing a and b by 1 in each iteration
            # We can check till how many steps, "a" and "b" piles won't change
            # Till "b" is not less than "c", "a" and "b" will remain the same piles
            
            decrementVal = b if c == 0 else b - c + 1
            
            a -= decrementVal
            b -= decrementVal
            
            # Increment the score by the decrementVal
            score += decrementVal
            
            # Update the "a", "b" and "c"
            if a < b: a,b = b,a
            if a < c: a,c = c,a
            if b < c: b,c = c,b
                
        # Finally, return the maximum score
        return score

a = 2
b = 4
c = 6

print("Maximum Score -> ", maximumScore(a,b,c))