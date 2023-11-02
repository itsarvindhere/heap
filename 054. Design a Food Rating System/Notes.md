Design a food rating system that can do the following:

 - Modify the rating of a food item listed in the system.
 - Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:

 - FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
    - foods[i] is the name of the ith food,
    - cuisines[i] is the type of cuisine of the ith food, and
    - ratings[i] is the initial rating of the ith food.
 - void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
 - String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

# EXAMPLE

Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]


Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

# APPROACH

Basically, we will have two Maps/Dictionaries.

One will keep track of the rating of each food item and also the cuisine that it belongs to.

The other will keep track of the cuisines and the food items that belong to that cuisine. And we will use a Max heap to keep those food items ordered by their ratings. Note that there can be a tie so in that case, we have to then look at the names of the food items. So, that's why, we can pass a "Triplet" to the Max heap so when there is a tie, the second value in this triplet is then used a tie breaker. That's why in the code, I am passing the "Food Item's name" as the second argument when I do heappush.

And the rest is pretty simple to understand.

Just note that when we change the rating of any food item, we don't delete the old data from the Max Heap.

We do this deletion only in the "highestRated" method and that too when that old data is on top of the maxHeap. So, it is kind of like Lazy Deletion.