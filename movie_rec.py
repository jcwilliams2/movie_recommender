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
            see_genres = str(input("Would you like to see what genres we know y/n: "))
            if see_genres.lower() is 'y':
                movie_genres = ""
                for genre in genres:
                    movie_genres += genre.capitalize() + "  "
                print(movie_genres)
    try_again = True
    while try_again:
        potential_string = "Would you like to see movies in: "
        count = 0
        for genre in potential_genres:
            potential_string += str(genre)
            count += 1
            if count > 0 and count < (len(potential_genres)):
                potential_string += " | "
        potential_string += '\n'
        potential_genre = str(input(potential_string))
        if potential_genre.lower() in potential_genres:
            return potential_genre
        print("Didn't quite catch that. Please try again.")


def movie_search(movie_list, target_genre=None):
    if target_genre is None:
        target_genre = get_genre()
    print(target_genre)
    
def test():
    greeting()
    movie_search(movie_list)
    farewell()

movie_list = establish_movie_dataset(movies)
test()