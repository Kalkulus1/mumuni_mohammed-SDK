"""Script used to define the Movie class."""

from lotr_sdk.base import LotrBase


class Movie(LotrBase):
    """docstring for Book."""

    @classmethod
    def list(cls):
        """
        List movies.

        Args:
            No argument required.

        Returns:
            Json data from The One API.
        """
        return cls().requests.get("movie/")

    @classmethod
    def get(cls, id):
        """
        Get a single movie.

        Args:
            id: the id of the movie.

        Returns:
            Json data from The One API.
        """
        return cls().requests.get(f"movie/{id}")

    @classmethod
    def get_qoutes(cls, id):
        """
        Get a single movie.

        Args:
            id: the id of the movie.

        Returns:
            Json data from The One API.
        """
        return cls().requests.get(f"movie/{id}/quote")
