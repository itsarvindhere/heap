# PROBLEM STATEMENT

You have a movie renting company consisting of n shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array entries where entries[i] = [shopi, moviei, pricei] indicates that there is a copy of movie moviei at shop shopi with a rental price of pricei. Each shop carries at most one copy of a movie moviei.

The system should support the following functions:

 - Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.
 - Rent: Rents an unrented copy of a given movie from a given shop.
 - Drop: Drops off a previously rented copy of a given movie at a given shop.
 - Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shopj, moviej] describes that the jth cheapest rented movie moviej was rented from the shop shopj. The movies in res should be sorted by price in ascending order, and in case of a tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.
  
Implement the MovieRentingSystem class:

 - MovieRentingSystem(int n, int[][] entries) Initializes the MovieRentingSystem object with n shops and the movies in entries.
 - List<Integer> search(int movie) Returns a list of shops that have an unrented copy of the given movie as described above.
 - void rent(int shop, int movie) Rents the given movie from the given shop.
 - void drop(int shop, int movie) Drops off a previously rented movie at the given shop.
 - List<List<Integer>> report() Returns a list of cheapest rented movies as described above.
  
Note: The test cases will be generated such that rent will only be called if the shop has an unrented copy of the movie, and drop will only be called if the shop had previously rented out the movie.

# EXAMPLE

Input
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]

Output
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]

Explanation
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1);  // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report();   // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2);  // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.

# **1. SORTED LIST APPROACH**
The SortedList is so helpful in such problems. It is provided by a third party library and as the name suggests, a SortedList will always keep the elements in a sorted order, no matter how many we add or remove from it. The addition, removal and lookup is an approximately O(LogN) time operation.

Basically, we will have a Dictionary/Hash Table to keep all the "movies" and the shops from which we can rent those movies. So this dictionary will have its "key" as the movie and the value as a SortedList. Why SortedList? Because for each movie, we will keep the data sorted by the price of the movie offered by each shop. 

When "rent" is called, we will simply remove the "shop" data from this dictionary for the particular "movie"

At any time, when "drop" is called, we want to put the movie details back into this dictionary. Since "drop" method only gives us the name of the shop and the movie, to keep track of the original price at which this shop listed the movie, we will also have a separate dictionary named "moviePrices"

This dictionary has the key as the shop and the value will be another dictionary with key as the movie and the value as price.

	Something like {shop : {movie1 : price, movie2 : price } }
	
And finally, when we rent a movie, we will save it in some other place. And so, for that, we will use a Min Heap named "rentedMovies". Why a minHeap? Because if "report" is called, then we want to return the 5 cheapest rented movies and since we are using a minHeap, it will automatically order all these rented movies by their prices.

With a SortedList, this code is very clean and easy to understand.

# **2. HEAP APPROACH**

If such a problem is asked in an interview, I doubt the interviewer will like an approach that uses a third party library.

Another approach is using a Heap, instead of a SortedList to keep track of the movies. The only downside is that you have to write some extra code because since it is a Heap, removal from it is not straightforward, unless done from the top.

So, we will simply need to pop all the values that we need to return in "search" or "report" and then push them back in the heap before returning. That's the extra step we do in this approach.