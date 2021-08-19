import os
import discord
import json
import bot_economy
import bot_games
import bot_pokemon_loja
import bot_pokemon
from dotenv import load_dotenv
from discord import client
from discord.ext import commands

load_dotenv()
token = os.environ.get('discord_token')
owner = os.environ.get('id')
client = commands.Bot(command_prefix = '.')

def checar(ctx):
    return ctx.author.id == int(owner)

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def banco(ctx):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_economy.banqueiro_visualizar(user)
    
    await ctx.send(resposta)

@client.command()
@commands.check(checar)
async def banco_retirar(ctx, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_economy.banqueiro_retirar(user, qtd)
    
    await ctx.send(resposta)

@client.command()
@commands.check(checar)
async def banco_adicionar(ctx, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_economy.banqueiro_adicionar(user, qtd)

    await ctx.send(resposta)

@client.command()
async def banco_transferir(ctx, qtd, *, nome:discord.Member):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    dados_recebe = [str(nome.id), nome.name, nome.mention]
    resposta = bot_economy.banqueiro_transferir(user, qtd, dados_recebe)
    
    await ctx.send(resposta)

@client.command(aliases=['rollsimples'])
async def jogo_dados_simples(ctx, escolha, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_games.jogatina_dados(user, escolha, qtd)
    
    await ctx.send(resposta)

@client.command(aliases=['rolldado'])
async def jogos_dados_composto(ctx, escolha, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_games.jogatina_dados_composto(user, escolha, qtd)

    await ctx.send(resposta)

@client.command()
@commands.check(checar)
async def banco_reset(ctx, *, nome:discord.Member):
    user = str(nome.id)
    bot_economy.banqueiro_resetar(user)
    
    await ctx.send('resetado')

@client.command(aliases=['x1'])
async def jogo_1v1(ctx, q=None):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_games.jogatina_1v1(user, q)
    
    await ctx.send(resposta)

@client.command()
@commands.check(checar)
async def qb_reset(ctx):
    bot_games.reseta_qb()

    await ctx.send('resetado')

@client.command(aliases=['registro'])
async def poke_registro(ctx):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_pokemon_loja.poke_reg(user)
    
    await ctx.send(resposta)

@client.command(aliases=['pokeloja'])
async def poke_loja(ctx, code=None, qtd=None):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_pokemon_loja.poke_loja(user, code, qtd)

    await ctx.send(resposta)

@client.command(aliases=['inicial'])
async def poke_inicial(ctx, nome=None):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_pokemon.poke_inicial(user, nome)

    await ctx.send(resposta)

@client.command(aliases=['time'])
async def poke_time(ctx):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    time_pokemon = bot_pokemon.poke_time(user)
    msg = ''
    for i in time_pokemon:
        msg += f'{i[0]:<30}Level: {i[1]}\n'

    await ctx.send(msg)

client.run(token)
