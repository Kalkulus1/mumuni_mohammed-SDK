# lotr-sdk
Python SDK for [lotr-api](https://the-one-api.dev/documentation) View on [pypi.python.org](https://pypi.org/project/lotr-sdk/)

## Installation
```sh
pip install lotr-sdk
```

## Use Lotr-SDK

```python
from lotr.ring import Ring

from lotr_sdk.lotr import Lotr

api_key = "your-api-key"

lotr = Lotr(api_key=api_key)

# to use quote api
print(lotr.qoute.list())
print(lotr.qoute.get(id="5cd96e05de30eff6ebcceba8"))

# to use movie api
print(lotr.movie.list())
print(lotr.movie.get(id="5cd95395de30eff6ebccde56"))
print(lotr.movie.get_qoutes(id="5cd95395de30eff6ebccde56"))

```

## Static Use
To start using the Lotr Python SDK, you need to start by setting your api key.

You can set your api key in your environment by running:

```sh
export API_KEY='your_api_key'
```

After exporting the keys, you can use the api like this
```python
from lotr_sdk.lotr import Movie, Quote

# to use movies class
print(Movie.list())

print(Movie.get(id="5cd95395de30eff6ebccde56"))
print(Movie.get_qoutes(id="5cd95395de30eff6ebccde56"))

# to use quote
print(Quote.list())

print(Quote.get(id="5cd96e05de30eff6ebcceba8"))
```

