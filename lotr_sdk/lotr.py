"""Entry point defined here."""
from lotr_sdk.quote import Quote
from lotr_sdk.movie import Movie
from lotr_sdk.base import LotrBase


class Lotr(LotrBase):
    """Base class defined for LOTR Instance Method."""

    def __init__(self, api_key=None):
        LotrBase.__init__(self, api_key=api_key)

        self.qoute = Quote
        self.movie = Movie
