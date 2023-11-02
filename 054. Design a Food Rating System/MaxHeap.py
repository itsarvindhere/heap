from collections import defaultdict
from heapq import heappop, heappush
class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        
        # Let's use a dictionary to keep track of the food item and the rating
        # We will also keep data about what type of "cuisine" is this food
        # So basically, each value is a pair [rating, cuisine]
        self.foodRating = {}
        
        # And let's use another dictionary to keep track of the cuisine 
        # and the food item with highest rating for this cuisine
        self.cousineRating = defaultdict(list)
        
        # Length
        n = len(foods)
        
        # Fill the Dictionaries with the data
        for i in range(n):
            
            # Update the "foodRating" dictionary
            self.foodRating[foods[i]] = [ratings[i], cuisines[i]]
            
            # Update the cousingRating dictionary
            # Since at any time, we want the highest rating, we can use a maxHeap here
            heappush(self.cousineRating[cuisines[i]], [-ratings[i], foods[i], foods[i]])
        

    def changeRating(self, food: str, newRating: int) -> None:
        
        # Update the rating of "food"
        self.foodRating[food][0] = newRating
        
        # Push this data to the cousineRating as well
        heappush(self.cousineRating[self.foodRating[food][1]], [-newRating, food, food])
        

    def highestRated(self, cuisine: str) -> str:
        # Before we return the highest rated cuisine, we will remove all the data that is no longer valid
        while self.cousineRating[cuisine] and -(self.cousineRating[cuisine][0][0]) != self.foodRating[self.cousineRating[cuisine][0][1]][0]:
            heappop(self.cousineRating[cuisine])
            
        # And now, we can return the name of food item on top of the max Heap
        return self.cousineRating[cuisine][0][1]
