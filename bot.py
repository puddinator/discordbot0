import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import random
import requests
import asyncio

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
    embed = discord.Embed(title="cool bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$rnick discordmember 0/1", value="Gives users a nickname", inline=False)

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def rnick(ctx, member : discord.Member, silent : int = 1):
    counter, runs = 0, 90
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


@client.command(pass_context=True)
async def join(ctx):
    voicechannel = ctx.author.voice.channel
    await voicechannel.connect()


client.run('NDc1MTgyOTY4NDQ5NTMxOTE2.Dkf5ew.dOAxpsKyYyssZt5UBybROMCcUL4')
