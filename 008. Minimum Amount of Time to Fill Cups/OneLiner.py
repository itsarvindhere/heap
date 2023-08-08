from math import ceil


def fillCups(amount):

        # We want minimum seconds required to fill all cups
        # For any input list, let's say [1,2,3]
        # We can easily say that the minimum seconds needed will definitely be more or same as "3" the greatest value
        # For example, if input was [0,0,3] then output would've been "3" only
        # Minimum seconds required can never be less than the greatest value. It is just not possible.
        # For example, take [1,2,5] as example
        # For this example, "5" seconds will be the output. Again, this is >= greatest value
        
        # So does it mean we can simply return the "greatest" value since that is the minimum possible value?
        # NO. This will be true in those test cases only where there are unique elements
        # What if we have a test case with some same values e.g. [1,3,3] or [3,3,3]
        # In both cases, the greatest value is 3 but the output is not 3. In fact, the output is 4 and 5 respectively
        # So, if there are multiple greatest values, then we cannot simply return the greatest value as output
        # If we see [1,3,3] its total sum is 7 and output is 3
        # IF we see [3,3,3] its total sum is 9 and output is 5
        # So looks like we are doing ceil(7/2) and ceil(9/2)
        # And well, we are.
        
        # So, there are two values to choose from now -> greatestValue and the round(sum/2)
        # And as we saw in above examples, if round(sum/2) is greater than greatest value in list, 
        # we choose that as the output, not the greatest Value in the list
        # In short, we always want the greater of the two values

        return max(max(amount),ceil(sum(amount) / 2))
amount = [5,4,4]

print("Output is ->", fillCups(amount))
        
        
