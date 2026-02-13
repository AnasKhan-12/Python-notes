import requests

url1="https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url=f"{url1}/pokemon/{name}"
    response= requests.get(url)
    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data Error:{ response.status_code}")
    #  print(response)

pokemon_name="pikachu"
x=get_pokemon_info(pokemon_name) #ab x ma dictionary store ha kiunky get_pokemon_info ussy return kr rha ha

if x:
    print(f"{x['name']}")
    print(f"{x['height']}")
