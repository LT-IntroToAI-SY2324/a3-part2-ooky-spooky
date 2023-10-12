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
