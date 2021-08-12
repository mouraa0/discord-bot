import os
import discord
import json
import bot_economy
from dotenv import load_dotenv
from discord import client
from discord.ext import commands

load_dotenv()
token = os.environ.get('discord_token')

client = commands.Bot(command_prefix = '.')

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
async def banco_retirar(ctx, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_economy.banqueiro_retirar(user, qtd)
    
    await ctx.send(resposta)

@client.command()
async def banco_adicionar(ctx, qtd):
    user = [ctx.author.id, ctx.author.name, ctx.author.mention]
    resposta = bot_economy.banqueiro_adicionar(user, qtd)

    await ctx.send(resposta)

client.run(token)
