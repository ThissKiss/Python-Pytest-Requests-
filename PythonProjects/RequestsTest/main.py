import requests
token = '4bea06a7fb33aa8bb5adb5f8d0cb07af'

# Запрос на создание покемона 
'''response_great_pokemon = requests.post("https://api.pokemonbattle.me:9104/pokemons", 
                          json={"name": "mu2",
                                "photo": "https://dolnikov.ru/pokemons/albums/150.png"},
                          headers={"Content-Type": "application/json", "trainer_token": token})
print(response_great_pokemon.text)'''

# Запрос на изменение имени покемона
response_name_pokemon = requests.put("https://api.pokemonbattle.me:9104/pokemons", 
                          json={"pokemon_id": "12494",
                                "name": "thisskiss",
                                "photo": "https://dolnikov.ru/pokemons/albums/149.png"},
                          headers={"Content-Type": "application/json", "trainer_token": token})
print(response_name_pokemon.text)

# Запрос поймать покемона
response_catch_pokemon = requests.post("https://api.pokemonbattle.me:9104/trainers/add_pokeball", 
                          json={"pokemon_id": "12494"},
                          headers={"Content-Type": "application/json", "trainer_token": token})
print(response_catch_pokemon.text)
