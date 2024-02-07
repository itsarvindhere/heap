class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        
        # For each movie, we will maintain a MIN HEAP
        # to keep track of the shops that have an unrented copy of that movie
        # a Min Heap will order them by the prices from smallest to largest
        self.movies = defaultdict(list)
        
        # A Dictionary to keep track of movie prices for various shops
        self.moviePrices = defaultdict(dict)
        
        for shop, movie, price in entries:
                
            heappush(self.movies[movie], (price, shop, movie))
            
            self.moviePrices[shop][movie] = price
            
        # A Min Heap to keep track of the rented movies
        # A Min Heap will ensure that the movies are ordered by the prices in ascending order
        self.rentedMovies = []
        
        # A set to keep track of the rented movies
        self.rentedMoviesSet = set()

    def search(self, movie: int) -> List[int]:
        
        # If there is no shop with an unrented copy of the "movie", return []
        if movie not in self.movies: return []
        
        # Return the cheapest 5 shops that have an unrented copy of given movie
        cheapest5Shops = []
        
        while len(cheapest5Shops) < 5 and self.movies[movie]:
            
            top = heappop(self.movies[movie])
            
			# If the movie is already rented from the shop in "top"
			# Or
			# It is the same movie that we added in previous iteration (skip duplicates)
            if top in self.rentedMoviesSet or (cheapest5Shops and top == cheapest5Shops[-1]): continue
                
            cheapest5Shops.append(top)
            
        # Push back into the rentedMovies minHeap
        for data in cheapest5Shops: heappush(self.movies[movie], data)
                
        # Return the required data
        return [data[1] for data in cheapest5Shops]
            

    def rent(self, shop: int, movie: int) -> None:
        
        # Add to the rented movies minHeap
        heappush(self.rentedMovies, (self.moviePrices[shop][movie], shop, movie))
        
        # Add it to the set of rentedMovies
        self.rentedMoviesSet.add((self.moviePrices[shop][movie], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        
        # Add to the "movies" dictionary
        heappush(self.movies[movie], (self.moviePrices[shop][movie], shop, movie))
        
        # Remove from the rented movies set
        self.rentedMoviesSet.remove((self.moviePrices[shop][movie], shop, movie))

    def report(self) -> List[List[int]]:
        
        # Return the cheapest 5 rented movies
        cheapest5RentedMovies = []
        
        while len(cheapest5RentedMovies) < 5 and self.rentedMovies:
            
            top = heappop(self.rentedMovies)
            
			# If the movie is not rented from the shop in "top"
			# Or
			# It is the same movie that we added in previous iteration (skip duplicates)
            if top not in self.rentedMoviesSet or (cheapest5RentedMovies and top == cheapest5RentedMovies[-1]): continue
                
            cheapest5RentedMovies.append(top)
            
        # Push back into the rentedMovies minHeap
        for data in cheapest5RentedMovies: heappush(self.rentedMovies, data)
            
        return [[data[1], data[2]] for data in cheapest5RentedMovies]