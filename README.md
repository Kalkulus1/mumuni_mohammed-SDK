# Lord of the Rings SDK (lotr_sdk)

The Lord of the Rings SDK provides an easy-to-use interface for developers to consume information about the Lord of the Rings from The One API.

Python SDK for [lotr-api - TheOneAPI](https://the-one-api.dev/documentation). View on [PyPi](https://test.pypi.org/project/kalkulus-sdk/)

## Installation

You can install the Lord of the Rings SDK using pip:
```sh
pip install -i https://test.pypi.org/simple/ kalkulus-sdk
```

## Usage of Lotr-SDK

### Authentication
If the Lord of the Rings API requires authentication with an api key.

Refer to the API documentation for authentication details. You just have to signup and get an api key.

```python
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

## Static Usage
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

## Examples
You can find more usage examples in the examples directory.


## Development
If you want to contribute to the development of the Lord of the Rings SDK, follow these steps:

### Clone the repo
```sh
git clone https://github.com/Kalkulus1/mumuni_mohammed-SDK.git
```

### Install the dependencies
Create your virtual environment and install the requirements.
```sh
pip install -r requirements.txt
```

Make your changes and add tests if applicable.

### Run the tests
```sh
pytest
```

### Lint Code
Use black to format your code.
```sh
black .
```
Create a pull request with your changes. If the pipeline checks pass, we will merge your code.

### License
This project is licensed under the MIT License.


