pokemon = ['lugia', 'pikachu', 'spheal', 
'wailord', 'charmander', 'articuno', 
'bulbasaur', 'squirtle', 
'dragonite', 'hitmonlee', 'zubat', 'psyduck', 'growlithe', 'arcanine', 
'poliwhirl', 'bellsprout', 'golem', 'ponyta', 'slowpoke', 'magnemite']

def pokeAPIcall(pokemon):
    import requests as r
    req = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    if req.status_code == 200:
        my_data = req.json()
    else:
        return req.status_code
    
    pokedict = {
        'name': my_data['name'],
        'types': [x['type']['name'] for x in my_data['types']],
        'abilities': [x['ability']['name'] for x in my_data['abilities']],
        'weight': my_data['weight']
    }

    return pokedict

monlist = [pokeAPIcall(name) for name in pokemon]

types = set()

for i in monlist:
    for t in i['types']:
        types.add(t)

pokemonbytype = {}

for t in types:
    pokemonbytype[t] = {pokemon['name']:pokemon for pokemon in monlist if t in pokemon['types']}

print(pokemonbytype) 

#pokemonbytype['water'] = {pokemon['name']:pokemon for pokemon in monlist if 'water' in pokemon['types']}
#print(pokemonbytype['water'])