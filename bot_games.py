import bot_economy
import json
from random import randint

def jogatina_geral():
    with open('games.json','r') as f:
        geral = json.load(f)
        
    return geral

def jogatina_dados(usuario, escolha, q):
    condicao = bot_economy.segurança_do_banco(q, usuario)
    if condicao[0] is True:
        return condicao[1]
    
    resposta = []
    decisao = randint(1,6)
    
    if decisao % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    if resultado == escolha:
        resposta.append('Ganhou!')
        resposta.append(bot_economy.banqueiro_adicionar(usuario, q))
    else:
        resposta.append('Perdeu!')
        resposta.append(bot_economy.banqueiro_retirar(usuario, q))
    
    return f'Você {resposta[0]} Número: {decisao}\n{resposta[1]}'

def jogatina_dados_composto(usuario, escolha, q):
    resposta = []
    condicao = bot_economy.segurança_do_banco(q, usuario)
    if condicao[0] is True:
        return condicao[1]
    if int(escolha) not in [1,2,3,4,5,6]:
        return 'Escolha um número de 1 a 6'
    
    decisao = randint(1,6)
    if decisao == int(escolha):
        resposta.append('Ganhou')
        resposta.append(bot_economy.banqueiro_adicionar(usuario, (int(q)*6)))
    
    else:
        resposta.append('Perdeu')
        resposta.append(bot_economy.banqueiro_retirar(usuario, q))
    
    return f'Você {resposta[0]}! Número: {decisao}\n{resposta[1]}'

def jogatina_1v1(usuario, q=None):
    
    data = jogatina_geral()
    resposta = []
    if len(data['qb']['players']['1']) == 0 :
        if q is None:
            return 'Faltou a aposta amigão'

        condicao = bot_economy.segurança_do_banco(q, usuario)
        if condicao[0] is True:
            return condicao[1]
        
        data['qb']['players']['1'] = usuario
        data['qb']['aposta'] = q
        with open('games.json','w') as f:
            json.dump(data, f, indent=2)
        
        return f'{usuario[2]} confirmado! Esperando adversário.'
    
    else:
        apostado = data['qb']['aposta']
        condicao = bot_economy.segurança_do_banco(data['qb']['aposta'], usuario)
        if condicao[0] is True:
            return condicao[1]
        
        data['qb']['players']['2'] = usuario
        decisao = randint(1,2)
        
        if decisao == 1:
            winner = data["qb"]["players"]['1']
            loser = data['qb']['players']['2']
            resposta.append(f'Vencedor: {winner[2]}!')
            resposta.append(bot_economy.banqueiro_retirar(loser, apostado))
            resposta.append(bot_economy.banqueiro_adicionar(winner, apostado))
        
        elif decisao == 2:
            winner = data["qb"]["players"]['2']
            loser = data['qb']['players']['1']
            resposta.append(f'Vencedor: {winner[2]}!')
            resposta.append(bot_economy.banqueiro_retirar(loser, apostado))
            resposta.append(bot_economy.banqueiro_adicionar(winner, apostado))
        
        reseta_qb()
        
        return f'{resposta[0]}\n{resposta[1]}\n{resposta[2]}'

def reseta_qb():
    data = jogatina_geral()
    data['qb'] = {}
    data['qb']['players'] = {}
    data['qb']['players']['1'] = []
    data['qb']['players']['2'] = []
    data['qb']['aposta'] = 0
    
    with open('games.json','w') as f:
        json.dump(data, f, indent=2)
