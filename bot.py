import os
import discord
import json
import bot_economy
import bot_games
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

def checar(ctx):
    return ctx.author.id == 263343578699399168

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

@client.command()
async def jogo_dados(ctx, escolha, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_games.jogatina_dados(user, escolha, qtd)
    
    await ctx.send(resposta)

@client.command()
async def banco_reset(ctx, *, nome:discord.Member):
    user = str(nome.id)
    bot_economy.banqueiro_resetar(user)
    await ctx.send('resetado')


client.run(token)
