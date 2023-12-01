# Install using  pip install sortedcontainers
from sortedcontainers import SortedList 
class SORTracker:

    def __init__(self):
        
        # To keep track of how many times the "get" method has been invoked
        self.i = 0
        
        # The reason why above approach gives TLE is that
        # On each "add" call, we are sorting the list
        # This is not an efficient approach
        
        # What if we have some data structure that takes the elements and automatically orders them
        # And such a data structure is a "Sorted List"
        # We just need to put items in it and it will take care of ordering them
        
        # Sorted List
        self.data = SortedList()
        

    def add(self, name: str, score: int) -> None:
        
        # Add the data to the Sorted List
        # Again, in the same way we added data in above approach
        # That is, a pair with "score" in negative and "name" as the second value
        self.data.add([-score,name])
        

    def get(self) -> str:
        
        # Return the "ith" best location
        bestLocation = self.data[self.i][1]
        
        # Increment i
        self.i += 1
        
        return bestLocation