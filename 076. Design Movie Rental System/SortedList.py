from sortedcontainers import SortedList
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        
        # For each movie, we will maintain a Sorted List 
        # to keep track of the shops that have an unrented copy of that movie
        self.movies = {}
        
        # A Dictionary to keep track of movie prices for various shops
        self.moviePrices = defaultdict(dict)
        
        for shop, movie, price in entries:
            
            if movie not in self.movies: self.movies[movie] = SortedList()
            self.movies[movie].add((price, shop))
            
            self.moviePrices[shop][movie] = price
            
        # A Sorted List to keep track of the rented movies
        self.rentedMovies = SortedList()

    def search(self, movie: int) -> List[int]:
        
        if movie not in self.movies: return []
        
        # Return the cheapest 5 shops that have an unrented copy of given movie
        cheapest5Shops = []
        
        for data in self.movies[movie]:
            cheapest5Shops.append(data[1])
            
            if len(cheapest5Shops) == 5: break
                
        return cheapest5Shops
            

    def rent(self, shop: int, movie: int) -> None:
        
        # Add to the rented movies list
        self.rentedMovies.add((self.moviePrices[shop][movie], shop, movie))
        
        # Remove from the "movies" dictionary
        self.movies[movie].remove((self.moviePrices[shop][movie], shop))

    def drop(self, shop: int, movie: int) -> None:
        
        # Add to the "movies" dictionary
        self.movies[movie].add((self.moviePrices[shop][movie], shop))
        
        # Remove from the rented movies list
        self.rentedMovies.remove((self.moviePrices[shop][movie], shop, movie))

    def report(self) -> List[List[int]]:
        
        # Return the cheapest 5 rented movies
        cheapest5RentedMovies = []
        
        for data in self.rentedMovies:
            cheapest5RentedMovies.append([data[1], data[2]])
            
            if len(cheapest5RentedMovies) == 5: break
                
        return cheapest5RentedMovies