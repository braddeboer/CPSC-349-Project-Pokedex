import requests
import webbrowser
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

def api_parser():
    # sets pokemon name used for searching and pulling information using the api parser
    pokemon = input("Enter Pokemon Name: ")
    # necessary url to access pokemon information
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    #stores the websites response ie raw website data
    web_response = requests.get(url)
    #converts the raw data into a readable key value dict
    data = web_response.json()

    #calls functions and passes the json data set
    information_sorter(data)
    pokemon_sprites(data)
    pokemon_cry(data)

def information_sorter(data):
    #sorts through the data json to get all possible "types" for the pokemon
    types = [t["type"]["name"] for t in data["types"]]
    #sorts through data json for weight
    weight = data["weight"]
    #gets height
    height = data["height"]
    #pokedex number
    poke_num = data["id"]
    #possible moves
    moves = [t["move"]["name"] for t in data["moves"]]
    
    
    print("PokeDex Num: " + str(poke_num) + "\nPokemon Weight: " + str(weight) + "\nPokemon Height: " + str(height) + "\nPokemon Types: " + str(types) + "\nPokemon's Possible Moves: " + str(moves))

def pokemon_sprites(data):
    #gets and loads the pokemon sprite on a new browser tab
    webbrowser.open(data["sprites"]["other"]["showdown"]["front_default"])
    
def pokemon_cry(data):
    #do not believe this function is working yet, still trying to get the libraries to work
    cry = data["cries"]["latest"]
    cry_audio = BytesIO(requests.get(cry).content)
    
    play(AudioSegment.from_file(cry_audio))
    
#starts the program
api_parser()
