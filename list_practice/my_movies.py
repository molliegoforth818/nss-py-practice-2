#Initialize empty list
fav_movies = []

#func to add movies to list
def add_movie(movie):
    fav_movies.append(movie)
    print(f"Movie {movie} added.")

#func to remove movies from the list
def remove_movie(movie):
    if movie in fav_movies:
        fav_movies.remove(movie)
        print(f"Movie {movie} was removed")
    else:
        print(f"Movie {movie} was not found")    

#func to display movies in the list
def display_movies(movies):
    if not movies: #checks if the list is empty first so that you can display a different message if it isn't
        print("You do not have any favorite movies yet")
    else:
        print(f"Here is a list of your favorite movies:")
        for movie in fav_movies:
            print(f" - {movie} ")
    

#func to count the movies in the list
def count_movies():
    movie_count = len(fav_movies)
    print (f"I have {movie_count} favorite movies")

#func to find a movie in the list
def find_movie(movie):
    if movie in fav_movies:
        print(f"{movie} is in your list of favorite movies")
    else:
        print(f"{movie} is not in your list of favorite movies")    

def clear_movies():
    fav_movies.clear()
    print(f"Your list of favorite movies has been cleared")
            
#adding my movies
add_movie("Moulin Rouge")
add_movie("Black is King")
add_movie("Harry Potter and the Audacity of this Bitch")
add_movie("Shrek")

#displaying my movies
display_movies(fav_movies)

#removing a movie
remove_movie("Shrek")

#displaying list with movie removed
display_movies(fav_movies)

#count how many favorite movies I have
count_movies()

#find one of my favorite movies
find_movie("Moulin Rouge")
find_movie("Shrek")

#clear movies from your list of favorite movies
clear_movies()

#display movies again to make sure list is cleared
display_movies(fav_movies)