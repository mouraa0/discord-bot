import bot_economy
from random import randint
def jogatina_dados(usuario, escolha, q):
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
    
    return f'Você {resposta[0]}\n{resposta[1]}'