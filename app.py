
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def show_movies():
    for movie in movies:
        show_movie_detail(movie)


def show_movie_detail(movie):
        print(f"Title: {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie tittle you're looking for: ")
    for movie in movies:
        if movie["title"] == search_title:
            show_movie_detail(movie)


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: ")
    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            break
        else:
            print("Unknown command, Please try again.")
        
        MENU_PROMT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

        
menu()

