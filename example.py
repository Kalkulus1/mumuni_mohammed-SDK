from lotr_sdk.lotr import Lotr

api_key = "T4GEP0BkCehqugI5QRYX"

lotr = Lotr(api_key=api_key)

# to use quote
print(lotr.qoute.list())
print(lotr.qoute.get(id="5cd96e05de30eff6ebcceba8"))

# for movie
print(lotr.movie.list())
print(lotr.movie.get(id="5cd95395de30eff6ebccde56"))
print(lotr.movie.get_qoutes(id="5cd95395de30eff6ebccde56"))
