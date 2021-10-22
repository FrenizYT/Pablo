import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '/', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Sukurė Freniz')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def profilioinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Štai, ką aš radau.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def siusti(ctx, *, content: str):
        for member in ctx.message.server.members:
            try:
                await client.send_message(member, content)
                await client.say(":white_check_mark: Sėkmingai išsiuntėte pranešima žaidėjui : {}  ".format(member))
            except:
                print("can't")
                await client.say(":x: Nepavyko išsiūsti pranešima žaidėjui {} ".format(member))


client.run("ODcyMDc5NTQ2ODA2MDcxMjk2.YQkpXg.KwlmsHaq1oURek8McQ60dRZcpfo")                
