import json
import bot_economy

def load_bags():
    with open('pokemon_bag.json', 'r') as f:
        geral = json.load(f)

        return geral

def close_bags(g):
    with open('pokemon_bag.json', 'w') as f:
        json.dump(g, f, indent=2)

    return

def load_loja():
    with open('loja.json', 'r') as f:
        geral = json.load(f)

        return geral

def close_loja(g):
    with open('loja.json', 'w') as f:
        json.dump(g, f, indent=2)
    
    return

def poke_bag_add(usuario, item, qtd):
    geral = load_bags()
    
    if str(item) not in geral[str(usuario[0])]['bag']:
        geral[str(usuario[0])]['bag'][str(item)] = int(qtd)
    
    else:
        geral[str(usuario[0])]['bag'][str(item)] += int(qtd)

    close_bags(geral)
    return

def poke_reg(usuario):
    geral = load_bags()
    if str(usuario[0]) not in geral:
        geral[str(usuario[0])] = dict()
        geral[str(usuario[0])]['dados'] = list()
        geral[str(usuario[0])]['dados'] = usuario[1:3]
        geral[str(usuario[0])]['pokemons'] = dict()
        geral[str(usuario[0])]['bag'] = dict() 
        geral[str(usuario[0])]['inicial'] = False
        close_bags(geral)
        
        return f'{usuario[2]} cadastrado!'
    else:
        
        return f'{usuario[2]} já está cadastrado!'

def poke_loja(usuario, cod=None, q=None):
    if q is None and cod is None:
        with open('loja.txt', 'r') as f:
            
            return f.read()

    else:
        loja = load_loja()
        poke_bag_add(usuario, loja[str(cod)]['nome'], q)
        preco = int(loja[str(cod)]['preco']) * int(q)
        resposta = bot_economy.banqueiro_retirar(usuario, preco)

        return f'{q} {loja[str(cod)]["nome"]}(s) adicionadas a sua mochila.\n{resposta}'
