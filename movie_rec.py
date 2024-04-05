from movie_data import *
from linkedlist import LinkedList

def greeting():
    program_name = 'Cinema List'
    print("Welcome to " + program_name + "!")

def farewell():
    print("Goodbye")

def establish_movie_dataset(movies):
    movie_list = LinkedList()
    for movie in movies:
        movie_list.insert_head_node(movie)
    return movie_list

def get_genre():
    potential_genres = []
    while len(potential_genres) == 0:
        user_input = str(input("What genre of movies would you like to see? ")).lower()
        for genre in genres:
            if genre.startswith(user_input):
                potential_genres.append(genre)
        if len(potential_genres) == 0:
            print("Didn't quite catch that. Input doesn't match any of our data.\n")
            see_genres = str(input("Would you like to see what genres we know y/n: ")).lower()
            if see_genres == 'y':
                movie_genres = ""
                for genre in genres:
                    movie_genres += str(genre).capitalize() + "  "
                print(movie_genres)
    try_again = True
    while try_again:
        potential_string = "Would you like to see movies in: "
        count = 0
        for genre in potential_genres:
            potential_string += str(genre).capitalize()
            count += 1
            if count > 0 and count < (len(potential_genres)):
                potential_string += " | "
        potential_string += '   '
        potential_genre = str(input(potential_string))
        #print("\n")
        if len(potential_genres) == 1:
            if potential_genre.lower() == 'y' or potential_genre.lower() == 'yes':
                return potential_genres[0]
        if potential_genre.lower() in potential_genres:
            return potential_genre
        print("Didn't quite catch that. Please try again.")

def get_movies(target_genre):
    current_movie_node = movie_list.get_head_node()
    #print(current_movie_node.get_value())
    target_movies = []
    movie_string = ""
    while current_movie_node != None:
        current_movie_data = current_movie_node.get_value()
        #print(current_movie_data)
        if current_movie_data is not None:
            current_movie_genres = current_movie_data[0]
            #print(current_movie_genres)
            if target_genre in current_movie_genres:
                target_movies += [current_movie_data]
        current_movie_node = current_movie_node.get_next_node()
    #print(target_movies)
    count = 0 
    movie_string += "********************************************"
    for movie in target_movies:
        movie_string += "\n {0}\n Directed by {1}\n Released in {2}\n".format(movie[1], movie[2], movie[3])
        if count < (len(target_movies)):
                movie_string += "********************************************"
        count += 1
    return movie_string



def movie_search(movie_list, target_genre=None):
    searching = True
    while searching:
        if target_genre is None:
            target_genre = get_genre()
        #print(target_genre)
        genre_movies = get_movies(target_genre)
        print(genre_movies)
        search_again = str(input("\nWould you like to search for a different genre? y/n ")).lower()
        if search_again != 'y':
            searching = False
        target_genre = None
    
def test():
    greeting()
    movie_search(movie_list)
    farewell()

movie_list = establish_movie_dataset(movies)
test()