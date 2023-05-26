"""Script used to define the Quote class."""

from lotr_sdk.base import LotrBase


class Quote(LotrBase):
    """docstring for Book."""

    @classmethod
    def list(cls):
        """
        List quotes.

        Args:
            No argument required.

        Returns:
            Json data from The One API.
        """
        return cls().requests.get("quote/")

    @classmethod
    def get(cls, id):
        """
        Get a single quote.

        Args:
            id: the id of the quote.

        Returns:
            Json data from The One API.
        """
        return cls().requests.get(f"quote/{id}")
