import json
import bot_pokemon_loja

def load_pokemons():
    with open('pokemons.json', 'r') as f:
        geral = json.load(f)
        
        return geral

def poke_add(usuario, dex, lvl=5):
    geral = load_pokemons()
    bag = bot_pokemon_loja.load_bags()
    bag[str(usuario[0])]['pokemons'][str(dex)] = geral['poke'][str(dex)]
    bag[str(usuario[0])]['pokemons'][str(dex)]['level'] = int(lvl)
    bag[str(usuario[0])]['inicial'] = True
    bot_pokemon_loja.close_bags(bag)

    return  f'{geral["poke"][str(dex)]["nome"]} foi adicionado a sua Mochila!'


def poke_inicial(usuario, resp=None):
    if resp is None:
        return f'Para escolher seu pokémon inicial, digite ".inicial *", substituindo o * pelo nome do inicial escolhido\nBulbasaur\nCharmander\nSquirtle'
    
    else:
        bag = bot_pokemon_loja.load_bags()
        if bag[str(usuario[0])]['inicial'] is False:
            if resp.lower() == 'charmander':
                resposta = poke_add(usuario, '004')
                
            elif resp.lower() == 'squirtle':
                resposta = poke_add(usuario, '007')
            
            elif resp.lower() == 'bulbasaur':
                resposta = poke_add(usuario, '001')
            
            else:
                return 'Escolha um pokémon válido.'
           
            return resposta
        
        else:
            return 'Inicial já escolhido.'

def poke_time(usuario):
    geral = bot_pokemon_loja.load_bags()
    resposta = []
    if geral[str(usuario[0])]['pokemons'] == '':
        
        return f'{usuario[2]} ainda não tem pokémons :('
    
    else:
        for i in geral[str(usuario[0])]['pokemons'].values():
            temp = []
            temp.append(i['nome'])
            temp.append(i['level'])
            resposta.append(temp[:])
        
        return resposta

def poke_areas_1(ctx):
    




def poke_areas(ctx, decider=None):
    if decider is None:
        return f'Escolha uma das áreas a seguir com o formato ".area <n° área>"\n1 - Route 1'
    
    else:
        if decider == '1':
            poke_areas_1(ctx)
        
