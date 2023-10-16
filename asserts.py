from database import games_db
from database import books_db
from database import movies_db
from match import match
from typing import List, Tuple, Callable, Any


### movie 
def get_movie_title(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]


def get_movie_director(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_movie_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_movie_actors(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]

def get_ratings(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[4]


## book title 
def get_book_title(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[0]

def get_book_title(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[0]

def get_author(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[1]

def get_book_title(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[2]

def get_book_year(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[3]

def get_villain(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[4]

def get_book_characters(book: Tuple[str, str, int, List[str]]) -> List[str]:
    return book[5]

## video games 
def get_game_title(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[0]

def get_game_developer(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[1]

def get_game_year(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[2]

def get_game_villain(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[3]

def get_game_characters(game: Tuple[str, str, int, List[str]]) -> List[str]:
    return game[4]  

#### movies 
def title_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    result = []
    for movie in movie_db:
        if int(matches[0]) == get_year(movie):
            result.append(get_title(movie))
    #print(result) 
    return result

def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get movies from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get movies made in 1991, 1992, 1993 & 1994)
    """
    result = []
    for movie in movie_db:
        if int(matches[0]) <= get_year(movie) and get_year(movie) <= int(matches[1]):
            result.append(get_title(movie))
    #print(result) 
    return result


def title_before_year(matches: List[str]) -> List[str]:
    """Finds all movies made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made before the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any movies made that year, only before)
    """
    result = []
    for movie in movie_db:
        if get_year(movie) < int(matches[0]):
            result.append(get_title(movie))
    print(result) 
    return result


def title_after_year(matches: List[str]) -> List[str]:
    """Finds all movies made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any movies made that year, only after)
    """
    result = []
    for movie in movie_db:
        if get_year(movie) > int(matches[0]):
            result.append(get_title(movie))
    #print(result) 
    return result



def director_by_title(matches: List[str]) -> List[str]:
    """Finds director of movie based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the movie
    """
    result = []
    for movie in movie_db:
        if get_title(movie) == matches[0]:
            result.append(get_director(movie))
    #print(result) 
    return result


def title_by_director(matches: List[str]) -> List[str]:
    """Finds movies directed by the passed in director

    Args:
        matches - a list of 1 string, just the director

    Returns:
        a list of movies titles directed by the passed in director
    """
    result = []
    for movie in movie_db:
        if get_director(movie) == matches[0]:
            result.append(get_title(movie))
    #print(result) 
    return result


def actors_by_title(matches: List[str]) -> List[str]:
    """Finds actors who acted in the passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of actors who acted in the passed in title
    """
    result = []
    for movie in movie_db:
        if get_title(movie) == matches[0]:
            result = (get_actors(movie))
    #print(result) 
    return result
    
    ## return a list 
    

def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of one item (an int), the year that the movie was made
    """
    result = []
    for movie in movie_db:
        if get_title(movie) == matches[0]:
            result.append(get_year(movie))
   # print(result) 
    return result
    # return a list 
    

def title_by_actor(matches: List[str]) -> List[str]:
    """Finds titles of all movies that the given actor was in

    Args:
        matches - a list of 1 string, just the actor

    Returns:
        a list of movie titles that the actor acted in
    """
    
    result = []
    for movie in movie_db:
        if matches[0] in get_actors(movie):
            result.append(get_title(movie))
    #print(result) 
    return result

def rating_by_title(matches: List[str]) -> List[str]:
    result = []
    if matches[0] in get_title(movie):
        result. append(get_ratings(movie))
    return result

def title_by_rating(matches: List[str]) -> List[str]:
    result = []
    if matches[0] in get_ratings(movie):
        result. append(get_title(movie))
    return result

def actors_by_rating(matches: List[str]) -> List[str]:
    result = []
    if matches[0] in get_ratings(movie):
        result. append(get_actors(movie))
    return result

# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt

# Pattern-action for games
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("who developed %"), title_by_developer), 
    (str.split("what games were released in _"), developer_by_title), 
    (str.split("what games were released between _ and _"), title_by_year_range), 
    (str.split("what games were released before _"), title_before_year), 
    (str.split("what games were released after _"), title_after_year), 
    (str.split("who was the villain of %"), title_by_villain), 
    (str.split("what characters were in %"), title_by_characters),  
    (str.split("what game villains appeared before _"), villains_before_year), 
    (str.split("what game villains appaeared after _"), villains_after_year), 
    (str.split("what game was developed by %"), developer_by_title), 
    (["bye"], bye_action),
]

# Pattern-action for books
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("who wrote %"), title_by_author), 
    (str.split("what books were written by _"), author_by_title), 
    (str.split("what books were released _"), title_by_year), 
    (str.split("what books were released between _ and _"), title_by_year_range), 
    (str.split("what books were released before _"), title_before_year), 
    (str.split("what books were released after _"), title_after_year), 
    (str.split("who was the villain of %"), title_by_villain), 
    (str.split("what characters were in %"), title_by_characters),  
    (str.split("what book villains appeared before _"), villains_before_year), 
    (str.split("what book villains appaeared after _"), villains_after_year), 
    (str.split("what book was written by %"), author_by_title), 
    (["bye"], bye_action),
]

# Pattern-action list for movies
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what actors were in %"), actors_by_title), 
    (str.split("what movies were made in _"), title_by_year),
    (str.split("what movies were made between _ and _"), title_by_year_range),
    (str.split("what movies were made before _"), title_before_year),
    (str.split("what movies were made after _"), title_after_year),
    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what movies did % appear"), title_by_actor),
    (str.split("what rating does % have"), rating_by_title),
    (str.split("what movies have an _ rating"), title_by_rating),
    (str.split("what actors were in % -rated movies"), actors_by_rating),
    (str.split("what directors directed % -rated movies?"), actors_by_title),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand, please try again"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        #print(mat)
        if mat is not None:
            answer = act(mat)
            return answer if answer else["No answers"]
    return ["I don't understand, please try again"]
   
def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("What is your question? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nBye! Have a spooktastic day!\n")

query_loop()

if __name__ == "__main__":
    assert isinstance(title_by_year(["1974"]), list), "title_by_year not returning a list"
    assert isinstance(title_by_year_range(["1970", "1972"]), list), "title_by_year_range not returning a list"
    assert isinstance(title_before_year(["1950"]), list), "title_before_year not returning a list"
    assert isinstance(title_after_year(["1990"]), list), "title_after_year not returning a list"
    assert isinstance(director_by_title(["jaws"]), list), "director_by_title not returning a list"
    assert isinstance(title_by_director(["steven spielberg"]), list), "title_by_director not returning a list"
    assert isinstance(actors_by_title(["jaws"]), list), "actors_by_title not returning a list"
    assert isinstance(year_by_title(["jaws"]), list), "year_by_title not returning a list"
    assert isinstance(title_by_actor(["orson welles"]), list), "title_by_actor not returning a list"
    assert isinstance(actors_by_title(["carrie"]), list) 
    assert isinstance(rating_by_title(["r"]), list) 
    
    assert sorted(title_by_year(["1974"])) == sorted(
        ["amarcord", "chinatown"]
    ), "failed title_by_year test"
    assert sorted(title_by_year_range(["1970", "1972"])) == sorted(
        ["the godfather", "johnny got his gun"]
    ), "failed title_by_year_range test"
    assert sorted(title_before_year(["1950"])) == sorted(
        ["casablanca", "citizen kane", "gone with the wind", "metropolis"]
    ), "failed title_before_year test"
    assert sorted(title_after_year(["1990"])) == sorted(
        ["boyz n the hood", "dead again", "the crying game", "flirting", "malcolm x"]
    ), "failed title_after_year test"
    assert sorted(director_by_title(["jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed director_by_title test"
    assert sorted(title_by_director(["steven spielberg"])) == sorted(
        ["jaws"]
    ), "failed title_by_director test"
    assert sorted(actors_by_title(["jaws"])) == sorted(
        [
            "roy scheider",
            "robert shaw",
            "richard dreyfuss",
            "lorraine gary",
            "murray hamilton",
        ]
    ), "failed actors_by_title test"
    assert sorted(actors_by_title(["movie not in database"])) == [], "failed actors_by_title not in database test"
    assert sorted(year_by_title(["jaws"])) == sorted(
        [1975]
    ), "failed year_by_title test"
    assert sorted(title_by_actor(["orson welles"])) == sorted(
        ["citizen kane", "othello"]
    ), "failed title_by_actor test"
    assert sorted(search_pa_list(["hi", "there"])) == sorted(
        ["I don't understand"]
    ), "failed search_pa_list test 1"
    assert sorted(search_pa_list(["who", "directed", "jaws"])) == sorted(
        ["steven spielberg"]
    ), "failed search_pa_list test 2"
    assert sorted(
        search_pa_list(["what", "movies", "were", "made", "in", "2020"])
    ) == sorted(["No answers"]), "failed search_pa_list test 3"

    assert sorted(actors_by_title(["carrie"])) == sorted(
        ["sissy spacek"]
    ), "failed actors_by_title test"


    print("All tests passed!")