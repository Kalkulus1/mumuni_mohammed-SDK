"Test movie class methods"
from lotr_sdk.movie import Movie


def test_list_movies_total():
    "Verify total is greater than zero"
    movies = Movie.list()
    assert movies["total"] > 0


def test_lotrs_in_movies():
    "Check if LOTR Series exists in list of movies"
    name = "The Lord of the Rings Series"
    movies = Movie.list()
    assert filter(lambda d: d["name"] == name, movies["docs"])


def test_get_movie():
    "Test a movie endpoint"
    name = "The Lord of the Rings Series"
    _id = "5cd95395de30eff6ebccde56"
    movie = Movie.get(id=_id)
    assert movie["total"] == 1
    assert filter(lambda d: d["_id"] == _id, movie["docs"])
    assert filter(lambda d: d["name"] == name, movie["docs"])


def test_get_movie_quotes():
    "Test get movie quotes"
    _id = "5cd95395de30eff6ebccde5d"
    movie_quotes = Movie.get_qoutes(id=_id)
    assert movie_quotes["total"] > 0
