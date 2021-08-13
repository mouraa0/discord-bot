import json

CURRENCY = 'mouredas'

def banqueiro_geral():
    with open('banco.json','r') as f:
        geral = json.load(f)
    
    return geral

def segurança_do_banco(qtd, usuario=None):
    geral = banqueiro_geral()
    if int(qtd) < 0:
        return True
    
    if usuario != None:
        if int(qtd) > geral[str(usuario[0])]['quantia']:
            return True

def banqueiro_registro(usuario):
    geral = banqueiro_geral()
    if str(usuario[0]) not in geral:
        geral[str(usuario[0])] = dict()
        geral[str(usuario[0])]['nome'] = usuario[1]
        geral[str(usuario[0])]['quantia'] = 100

    with open('banco.json', 'w') as f:
        json.dump(geral, f, indent=2)
    
def banqueiro_visualizar(usuario):
    banqueiro_registro(usuario)
    geral = banqueiro_geral()

    return f'{usuario[2]}: {geral[str(usuario[0])]["quantia"]} {CURRENCY}'

def banqueiro_retirar(usuario, qtd):
    banqueiro_registro(usuario)
    geral = banqueiro_geral()
    quantia_atual = geral[str(usuario[0])]['quantia']
    geral[str(usuario[0])]['quantia'] = quantia_atual - int(qtd)
    
    with open('banco.json', 'w') as f:
        json.dump(geral, f, indent=2)
    
    return f'{qtd} {CURRENCY} retiradas da conta de {usuario[2]}'

def banqueiro_adicionar(usuario, qtd):
    banqueiro_registro(usuario)
    geral = banqueiro_geral()
    quantia_atual = geral[str(usuario[0])]['quantia']
    geral[str(usuario[0])]['quantia'] = quantia_atual + int(qtd)

    with open('banco.json', 'w') as f:
        json.dump(geral, f, indent=2)
    
    return f'{qtd} {CURRENCY} adicionadas a conta de {usuario[2]}'

def banqueiro_transferir(usuario, qtd, membro):
    condicao = segurança_do_banco(qtd, usuario)
    if condicao is True:
        return 'Problema :('
    geral = banqueiro_geral()
    
    resposta = []
    resposta.append(banqueiro_retirar(usuario, qtd))
    resposta.append(banqueiro_adicionar(membro, qtd))

    return f'Transferência concluída!\n{resposta[0]}\n{resposta[1]}'

def banqueiro_resetar(usuario):
    geral = banqueiro_geral()
    geral[str(usuario)]['quantia'] = 100

    with open('banco.json', 'w') as f:
        json.dump(geral, f, indent=2)

