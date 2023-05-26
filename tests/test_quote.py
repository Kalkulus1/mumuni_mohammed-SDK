"Test quote class methods"
from lotr_sdk.quote import Quote


def test_list_quotes_total():
    "Verify total is greater than zero"
    quotes = Quote.list()
    assert quotes["total"] > 0


def test_dialog_in_quotes():
    "Check if dialog exists in list of quotes"
    dialog = "Why?"
    quotes = Quote.list()
    assert filter(lambda d: d["name"] == dialog, quotes["docs"])


def test_get_movie():
    "Test a quote endpoint"
    dialog = "Why?"
    _id = "5cd96e05de30eff6ebcceba8"
    quote = Quote.get(id=_id)
    assert quote["total"] == 1
    assert filter(lambda d: d["_id"] == _id, quote["docs"])
    assert filter(lambda d: d["name"] == dialog, quote["docs"])
