import discord
import youtube_dl
import nltk
from nltk.corpus import wordnet
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import random
import requests
import asyncio
import sys
import os

client = commands.Bot(command_prefix='$')
description = 'cool'

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)

players = {}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@client.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@client.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@client.command()
async def info(ctx):
    embed = discord.Embed(title="coolest bot", description="Better than Athena", color=0xee657)
    
    # give info about you here
    embed.add_field(name="Author", value="Puddin")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/api/oauth2/authorize?client_id=475182968449531916&permissions=0&scope=bot>)")

    await ctx.send(embed=embed)

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Booty", description="Awesome bot! List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$rnick Member 0/1 Time/s", value="Gives users a nickname, 0 is verbose, 1 is silent", inline=False)
    embed.add_field(name="$clear X", value="Clears an **X** amount of messages", inline=False)
    embed.add_field(name="$Restart", value="Restarts Botty!", inline=False)
    embed.add_field(name="$Define X", value="Defines **X**", inline=False)
    embed.add_field(name="$Repeat X", value="Repeats **X**", inline=False)

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount)
    await ctx.send('{} {}'.format(amount, 'messages deleted'))

@client.command()
@commands.has_permissions(manage_guild=True)
async def restart(ctx):
    await ctx.send('Botty is restarting...')
    os.execv(sys.executable, ['python3'] + sys.argv)
     
@client.command()
async def define(ctx, a):
    define1 = wordnet.synsets(str(a))
    await ctx.send(str(a) + ": " + define1[0].definition())

@client.command()
@commands.has_permissions(manage_messages=True)
async def rnick(ctx, member : discord.Member, silent : int = 1, time : int = 30):
    counter, runs = 0, time
    old_nick = member.display_name
    while True:
        new_nick = random.choice(response.content.splitlines()).decode("utf-8")
        if silent == 0:
            await ctx.send(str(old_nick) + " (" + str(member.name) + ") "+ " is now " + new_nick)
        await member.edit(nick = new_nick)
        counter += 1
        if (counter) >= runs: 
            break
        await asyncio.sleep(10)

@client.command()
async def repeat(ctx, arg):
    await ctx.send(arg)

@client.command()
async def roulette(ctx):
    lucky = random.randint(0,21)
    if (lucky%4 == 0):
        await ctx.send('The trigger is pulled, and the hand-cannon goes off with a roar! You lie dead in the chat.')
    else:
        await ctx.send('The trigger is pulled, and the revolver clicks. You have lived to survive and see another day!')


@client.command()
async def join(ctx):
    voicechannel = ctx.author.voice.channel
    await voicechannel.connect()

client.run(str(os.environ.get('TOKEN')))

