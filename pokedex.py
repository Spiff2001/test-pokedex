import requests

def poke_to_string(poke_object: dict):
    master_string="Pokémon No. {id_num} : {pokemon_name} \n abilities: {pokemon_abilities} \n types: {pokemon_types} \n Weight: {pokemon_weight}"
    #abilities section
    abilities=poke_object['abilities']
    ability_litany = ""
    for ability in abilities:
         current_ability = ability['ability']['name']
         ability_litany+=current_ability+", "
    #type(s) section
    types=poke_object['types']
    type_litany=""
    for individual_type in types:
        current_type=individual_type['type']['name']
    type_litany+=current_type+", "
    weight=str(poke_object['weight'])
    id=str(poke_object["id"])
    name=poke_object["name"]
    print(master_string.format(id_num=id,pokemon_name=name,pokemon_abilities=ability_litany,pokemon_types=type_litany,pokemon_weight=weight))
    
def pokedex_engine(engine_query: str):
    pokemon_json=(requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000001&offset=0").json())
    pokemon_list=pokemon_json['results']
    print("searching for matching Pokémon:")
    for pokemon in pokemon_list:
        pokemon_url=pokemon['url']
        pokemon_url_altered=pokemon_url.replace("https://pokeapi.co/api/v2/pokemon/","")
        pokemon_id=pokemon_url_altered.replace("/","")
        if(str(engine_query) in pokemon['name']):
            print(pokemon['name']+": ID "+pokemon_id)
    print("search complete")   



print("pokedex engine v2: search for multiple pokemon by entering characters or strings")
print("specific pokemon can be found by entering poké ID numbers as follows: ID #")


       




while True:
    name=input()
    
   
    if (name == "exit"):
        break
    elif("ID" in name):
        pokemon_name=name.replace("ID ","")
        poke_to_string((requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon_name)).json())
    elif(type(name)==str):
        pokedex_engine(name)
        #apparently I'll need a new way to funnel this off into a specific pokemon. maybe go by name within the original.
   

