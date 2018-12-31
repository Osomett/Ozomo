import discord

from discord.ext.commands import Bot

from discord.ext import commands

from discord.ext.commands.cooldowns import BucketType

import asyncio

import platform

import colorsys

import random

import os

import time

from discord.voice_client import VoiceClient

from discord import Game, Embed, Color, Status, ChannelType

import traceback

import string

import inspect

import json

from cleverwrap import CleverWrap

import config

import utils

import aiohttp

import websockets

from bs4 import BeautifulSoup

import urllib.request

import logging

import colorsys

import socket

import praw

import datetime	import discord

from discord.ext import commands

from discord.ext.commands.cooldowns import BucketType

import asyncio

import colorsys

import random

import platform

from discord import Game, Embed, Color, Status, ChannelType

import os

import functools

import time

import datetime

import requests

import json

import aiohttp

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)

client = Bot(description="Osome beta bot", command_prefix="-", pm_help = True)

client.remove_command('help')

reddit = praw.Reddit(client_id='509384991697010688',

                     client_secret='QDb_Vjj7SRd_61qgFGzqyhgAYG2TlGWM',

                     user_agent='android:com.G-SK66FZT8at9g.SolarBot:v1.2.3 (by /u/LaidDownRepaer)')

async def status_task():

    while True:

        await client.change_presence(game=discord.Game(name='for -help'))

        await asyncio.sleep(5)

        await client.change_presence(game=discord.Game(name=''+str(len(set(client.get_all_members())))+' users', type = 3))

        await asyncio.sleep(5)

        await client.change_presence(game=discord.Game(name=''+str(len(client.servers))+' servers', type = 3))

        await asyncio.sleep(5)

 

@client.event

async def on_ready():

    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')

    print('--------')

    print('--------')

    print('Started Osome bot')

    print('Created by Dank Osome')

    client.loop.create_task(status_task())

  

def is_owner(ctx):

    return ctx.message.author.id == "493727314824396811"

 

def is_thunder(ctx):

    return ctx.message.author.id == "477463812786618388"

 

def is_osome(ctx):

    return ctx.message.author.id == "493727314824396811"

 

def is_sai(ctx):

    return ctx.message.author.id == "411133055185453057"

 

def is_zakktur(ctx):

    return ctx.message.author.id == "495131494805929985"

    

 

@client.event

async def on_member_join(member):

    print("Don't Go Alone Take'" + member.name + "Thanks For Joining!")

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))

    embed.set_author(name='Welcome message')

    embed.add_field(name = '__Welcome to Our Server__',value ='**Hope you will be active here. Check Our server #rules and never break any rules. ',inline = False)

    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')

    await client.send_message(member,embed=embed)

    print("Sent message to " + member.name)

    channel = discord.utils.get(client.get_all_channels(), server__name='Zakktur Coding help', name='conference')

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check <#474572305192845312> and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))

    embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)

    embed.add_field(name='Your join position is', value=member.joined_at)

    embed.set_thumbnail(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')

    embed.set_image(url=member.avatar_url)

    await client.send_message(channel, embed=embed)

    

@client.event

async def on_error(event, *args, **kwargs):

    if client.dev:

        traceback.print_exc()

    else:

        embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red

        embed.add_field(name='Event', value=event)

        embed.description = '```py\n%s\n```' % traceback.format_exc()

        embed.timestamp = datetime.datetime.utcnow()

        try:

            await client.owner.send(embed=embed)

        except:

            pass

            

@client.event

async def on_message(message):

	await client.process_commands(message)

	if message.content == 'Hi':

		await client.send_message(message.channel, '**Hey** hello')

@client.command(pass_context = True)

async def meme(ctx):

    colour = '0x' + '008000'

    async with aiohttp.ClientSession() as session:

        async with session.get("https://api.reddit.com/r/me_irl/random") as r:

            data = await r.json()

            embed = discord.Embed(title='Look at this meme', description='Its absolute Lol', color=discord.Color(int(colour, base=16)))

            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])

            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')

            embed.timestamp = datetime.datetime.utcnow()

            await client.say(embed=embed)

            

@client.command()

async def coinflip(playerChoice):

    outcomes = ['heads', 'tails']

    botChoice = random.choice(outcomes)

    

    playerChoice = playerChoice.lower()

    

    if botChoice == playerChoice:

    	

    	await client.say("And it was " + playerChoice + " Congratulations dumb")

    	

    elif botChoice == "heads" and playerChoice == "tails":

    		

    		await client.say("It was " + botChoice + " Dumb unlucky")

    		

    elif botChoice == "tails" and playerChoice == "heads":

    			

    			await client.say("It was " + botChoice + " You suck dumbass")

    

@client.command(name='8-ball',

                description="Answers a yes/no question.",

                brief="Answers from the beyond.",

                aliases=['eight_ball', 'eightball', '8ball'],

                pass_context=True)

async def magicball(ctx):

	outcomes = ["It is certain :8ball:", "It is decidedly so :8ball:", "Without a doubt :8ball:", "Yes, definitely :8ball:", "You may rely on it :8ball:", "As I see it, yes :8ball:", "Most likely :8ball:", "Outlook good :8ball:", "Yes :8ball:", "Signs point to yes :8ball:", "Reply hazy try again :8ball:", "Ask again later :8ball:", "Better not tell you now :8ball:", "Cannot predict now :8ball:", "Concentrate and ask again :8ball:", "Don't count on it :8ball:", "My reply is no :8ball:", "My sources say no :8ball:", "Outlook not so good :8ball:", "Very doubtful :8ball:"]

	await client.say("I choose: {}".format(random.choice(outcomes)))

    

@client.command()

async def rps(playerChoice):

    outcomes = ["rock", "paper", "scissor"]

    botChoice = random.choice(outcomes)

    playerChoice = playerChoice.lower()

    if botChoice == playerChoice:

        await client.say("You said " + playerChoice + " and the Bot said " + botChoice + "\n" + "Its a tie!")

    elif botChoice == "rock" and playerChoice == "paper":

        await client.say("You said paper and the Bot said rock." + "\n" + "You won! the Bot lost!")

    elif botChoice == "rock" and playerChoice == "scissor":

        await client.say("You said scissor and the Bot said rock." + "\n" + "the Bot won! You lost! haha")

    elif botChoice == "paper" and playerChoice == "rock":

        await client.say("You said rock and the Bot said paper." + "\n" + "the Bot won! You lost! haha")

    elif botChoice == "paper" and playerChoice == "scissor":

        await client.say("You said scissor and the Bot said paper." + "\n" + "You won! the Bot lost!")

    elif botChoice == "scissor" and playerChoice == "paper":

        await client.say("You said paper and the Bot said scissor." + "\n" + "The Bot won! You lost! haha")

    elif botChoice == "scissor" and playerChoice == "rock":

        await client.say("You said rock and the Bot said scissor." + "\n" + "You won! the Bot lost!")

@client.command(pass_context = True)

@commands.has_permissions(kick_members=True) 

async def lock(ctx, channelname: discord.Channel=None):

    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)

    if not channelname:

        role = discord.utils.get(ctx.message.server.roles, name='@everyone')

        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)

        await client.say("Channel locked by: {}".format(ctx.message.author))

    else:

        role = discord.utils.get(ctx.message.server.roles, name='@everyone')

        await client.edit_channel_permissions(channelname, role, overwrite)

        await client.say("Channel locked by: {}".format(ctx.message.author))

@client.command(pass_context = True)

@commands.has_permissions(kick_members=True) 

async def unlock(ctx, channelname: discord.Channel=None):

    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)

    if not channelname:

        role = discord.utils.get(ctx.message.server.roles, name='@everyone')

        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)

        await client.say("Channel unlocked by: {}".format(ctx.message.author))

    else:

        role = discord.utils.get(ctx.message.server.roles, name='@everyone')

        await client.edit_channel_permissions(channelname, role, overwrite)

        await client.say("Channel unlocked by: {}".format(ctx.message.author))

@client.command(pass_context=True)

async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):

    shipuser1 = user.name

    shipuser2 = user2.name

    useravatar1 = user.avatar_url

    useravatar2s = user2.avatar_url

    self_length = len(user.name)

    first_length = round(self_length / 2)

    first_half = user.name[0:first_length]

    usr_length = len(user2.name)

    second_length = round(usr_length / 2)

    second_half = user2.name[second_length:]

    finalName = first_half + second_half

    score = random.randint(0, 100)

    filled_progbar = round(score / 100 * 10)

    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)

    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"

    async with aiohttp.ClientSession() as cs:

        async with cs.get(url) as r:

            res = await r.json()

            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))

            embed.set_image(url=res['message'])

            await client.say(embed=embed)

		

@client.command(pass_context = True)

@commands.has_permissions(manage_messages = True)

async def dm(ctx, user: discord.Member, *, msg: str):

    try:

        await client.send_message(user, msg)

        await client.delete_message(ctx.message)          

        await client.say("Success! Your DM has made it! :white_check_mark: ")

    except:

        await client.say("Error :x:. Make sure your message is shaped in this way: -dm [tag person] [msg]")

        

@client.command(pass_context = True)

async def info_user(ctx, user: discord.Member):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))

    embed.add_field(name="Name", value=user.name, inline=True)

    embed.add_field(name="ID", value=user.id, inline=True)

    embed.add_field(name="Status", value=user.status, inline=True)

    embed.add_field(name="Highest role", value=user.top_role)

    embed.add_field(name="Joined", value=user.joined_at)

    embed.set_thumbnail(url=user.avatar_url)

    await client.say(embed=embed)

@client.command()

async def square(number):

    squared_value = int(number) * int(number)

    await client.say(str(number) + " squared is " + str(squared_value))

    

@client.command(pass_context = True)

@commands.has_permissions(manage_nicknames=True)    

async def setnick(ctx, user: discord.Member, *, nickname):

    await client.change_nickname(user, nickname)

    await client.delete_message(ctx.message)

@commands.has_permissions(manage_messages = True)

@client.command(pass_context=True)

async def poll(ctx, question, *options: str):

        if len(options) <= 1:

            await client.say('You need more than one option to make a poll!')

            return

        if len(options) > 10:

            await client.say('You cannot make a poll for more than 10 things!')

            return

 

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':

            reactions = ['👍', '👎']

        else:

            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

 

        description = []

        for x, option in enumerate(options):

            description += '\n {} {}'.format(reactions[x], option)

            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))

        react_message = await client.say(embed=embed)

        for reaction in reactions[:len(options)]:

            await client.add_reaction(react_message, reaction)

        embed.set_footer(text='Poll ID: {}'.format(react_message.id))

        await client.edit_message(react_message, embed=embed)

        

@client.command(pass_context=True)  

@commands.has_permissions(kick_members=True)    

async def kick(ctx,user:discord.Member):

 

    if user.server_permissions.kick_members:

        await client.say('**He is mod/admin and i am unable to kick him/her**')

        return

   

    try:

        await client.kick(user)

        await client.say(user.name+' was kicked. Good bye '+user.name+'!')

        await client.delete_message(ctx.message)

 

    except discord.Forbidden:

        await client.say('Permission denied.')

        return

 

@client.command(pass_context = True)

@commands.has_permissions(manage_messages=True)  

async def clear(ctx, number):

 

    if ctx.message.author.server_permissions.manage_messages:

         mgs = [] 

         number = int(number)

    async for x in client.logs_from(ctx.message.channel, limit = number+1):

        mgs.append(x)            

       

    try:

        await client.delete_messages(mgs)          

        await client.say(str(number)+' messages deleted')

     

    except discord.Forbidden:

        await client.say(embed=Forbidden)

        return

    except discord.HTTPException:

        await client.say('clear failed.')

        return        

   

 

    await client.delete_messages(mgs)      

 

@client.command(pass_context=True)  

@commands.has_permissions(ban_members=True)      

async def ban(ctx,user:discord.Member):

 

    if user.server_permissions.ban_members:

        await client.say('**He is mod/admin and i am unable to ban him/her**')

        return

 

    try:

        await client.ban(user)

        await client.say(user.name+' was banned. Good bye '+user.name+'!')

 

    except discord.Forbidden:

 

        await client.say('Permission denied.')

        return

    except discord.HTTPException:

        await client.say('ban failed.')

        return       

 

 

 

@client.command(pass_context=True)  

@commands.has_permissions(ban_members=True)    

 

 

async def unban(ctx):

    ban_list = await client.get_bans(ctx.message.server)

 

    # Show banned users

    await client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

 

    # Unban last banned user

    if not ban_list:

       

        await client.say('Ban list is empty.')

        return

    try:

        await client.unban(ctx.message.server, ban_list[-1])

        await client.say('Unbanned user: `{}`'.format(ban_list[-1].name))

    except discord.Forbidden:

        await client.say('Permission denied.')

        return

    except discord.HTTPException:

        await client.say('unban failed.')

        return                               

 

@client.command(pass_context = True)

@commands.has_permissions(administrator=True)

async def say(ctx, *, msg = None):

    await client.delete_message(ctx.message)

 

    if not msg: await client.say("Please specify a message to send")

    else: await client.say(msg)

    return

@client.command(pass_context =True)

async def greentext(ctx, *, msg = None):

	await client.delete_message(ctx.message)

	

	if not msg: await client.say("Please specify a message to send")

	else: await client.say("```" + msg + "```")

    

@client.command(pass_context=True)  

async def serverinfo(ctx):

    server = ctx.message.server

    roles = [x.name for x in server.role_hierarchy]

    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...

        roles = roles[:50]

        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    online = len([m.status for m in server.members if m.status == discord.Status.online or m.status == discord.Status.idle])

    embed = discord.Embed(name="{} Server information".format(server.name), color = discord.Color((r << 16) + (g << 8) + b))

    embed.set_thumbnail(url = server.icon_url)

    embed.add_field(name="Server name", value=server.name, inline=True)

    embed.add_field(name="Owner", value=server.owner.mention)

    embed.add_field(name="Server ID", value=server.id, inline=True)

    embed.add_field(name="Roles", value=len(server.roles), inline=True)

    embed.add_field(name="Members", value=len(server.members), inline=True)

    embed.add_field(name="Online", value=f"**{online}/{len(server.members)}**")

    embed.add_field(name="Created at", value=server.created_at.strftime("%d %b %Y %H:%M"))

    embed.add_field(name="Emojis", value=f"{len(server.emojis)}/100")

    embed.add_field(name="Server Region", value=str(server.region).title())

    embed.add_field(name="Total Channels", value=len(server.channels))

    embed.add_field(name="AFK Channel", value=str(server.afk_channel))

    embed.add_field(name="AFK Timeout", value=server.afk_timeout)

    embed.add_field(name="Verification Level", value=server.verification_level)

    embed.add_field(name="Roles {}".format(role_length), value = roles)

    await client.send_message(ctx.message.channel, embed=embed)

    

@client.command(pass_context = True)

async def rainbow(ctx):

    role = discord.utils.get(ctx.message.server.roles, name='Rainbow')

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    await client.edit_role(ctx.message.server, role, color = discord.Color((r << 16) + (g << 8) + b))

@client.command(pass_context = True)

async def ping(ctx):

    channel = ctx.message.channel

    t1 = time.perf_counter()

    await client.send_typing(channel)

    t2 = time.perf_counter()

    await client.say("Ping: {}ms".format(round((t2-t1)*1000)))

@client.command(pass_context = True)

@commands.has_permissions(administrator=True) 

async def announce(ctx, channel: discord.Channel=None, *, msg: str):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed=discord.Embed(title="Announcement", description="{}".format(msg), color = discord.Color((r << 16) + (g << 8) + b))

    await client.send_message(channel, embed=embed)

    await client.delete_message(ctx.message)

    

@client.command(pass_context=True)

@commands.has_permissions(manage_server = True)

async def userinfo(ctx, user: discord.Member):

    embed = discord.Embed(title="{}'s information".format(user.name), color=0xacd5b6)

    embed.add_field(name="Name", value=user.mention, inline=True)

    embed.add_field(name="ID", value=user.id, inline=True)

    embed.add_field(name="Status", value=user.status, inline=True)

    embed.add_field(name="Highest Role", value=user.top_role)

    embed.add_field(name="Joined", value=user.joined_at.strftime("%d %b %Y %H:%M"))

    embed.add_field(name="Created", value=user.created_at.strftime("%d %b %Y %H:%M"))

    embed.add_field(name="Color", value=user.color)

    embed.add_field(name="Bot", value=str(user.bot))

    embed.add_field(name="Playing", value=user.game)

    embed.add_field(name="Discord Tag", value=user.discriminator)

    embed.add_field(name="Nickname", value=user.nick)

    embed.add_field(name="Server", value=user.server)

    try:

            roles = [x.name for x in user.roles if x.name != "@everyone"]

            if roles:

                roles = sorted(roles, key=[x.name for x in ctx.message.server.role_hierarchy

                                           if x.name != "@everyone"].index)

                roles = ", ".join(roles)

            else:

                roles = "None"

            embed.add_field(name="Roles", value=roles)

    except:

        pass

    embed.set_thumbnail(url=user.avatar_url)

    await client.say(embed=embed)

@client.command(pass_context=True)

async def botinfo(ctx):

    embed = discord.Embed(title="Osome beta bot's information'", color=0xD2DCE5)

    embed.add_field(name="Bot Name", value="Osome beta bot")

    embed.add_field(name="Bot Tag", value="9962")

    embed.add_field(name="Bot ID", value="509384991697010688")

    embed.add_field(name="Bot owner", value="Dank Osome#2413")

    embed.add_field(name="Bot Prefix", value="-")

    embed.add_field(name="Bot LIB", value="discord.py")

    embed.add_field(name="Bot Language", value="Python")

    embed.add_field(name="Bot Servers", value=len(client.servers))

    embed.add_field(name="Bot Users", value=(len(set(client.get_all_members()))))

    embed.add_field(name="Bot Commands", value=(str(len(client.commands))))

    embed.set_thumbnail(url=" ")

    await client.say(embed=embed)

@client.command(pass_context =True)

async def test(ctx):

	msg = await client.say("Testing the bot")

	await client.send_typing(ctx.message.channel)

	await asyncio.sleep(5)

	msg2 = await client.edit_message(msg, '<:sadgun:519141924456628235>')

	await asyncio.sleep(5)

	await client.edit_message(msg2, "Test is complete")

	

@client.command(pass_context=True)

async def hack(ctx, user: discord.Member):

    discord_password = "Loopy321"

    computer_login = "I love doody"

    facebook = "Fooshy"

    msg = await client.say("Starting LEET Hack tool")

    await asyncio.sleep(1)

    msg2 = await client.edit_message(msg, "Starting LEET Hack tool.")

    await asyncio.sleep(1)

    msg3 = await client.edit_message(msg2, "Starting LEET Hack tool..")

    await asyncio.sleep(1)

    msg4 = await client.edit_message(msg3, "Starting LEET Hack tool...")

    await asyncio.sleep(1)

    msg5 = await client.edit_message(msg4, "Starting LEET Hack tool")

    await asyncio.sleep(1)

    msg6 = await client.edit_message(msg5, "Starting LEET Hack tool.")

    await asyncio.sleep(1)

    msg7 = await client.edit_message(msg6, "Starting LEET Hack tool..")

    await asyncio.sleep(1)

    msg8 = await client.edit_message(msg7, "Starting LEET Hack tool...")

    await asyncio.sleep(1)

    msg9 = await client.edit_message(msg8, "Starting LEET Hack tool")

    msg10 = await client.edit_message(msg9, "Successfully started the hack tool!")

    msg11 = await client.say(f"Looking for {user.mention}'s discord password in the discord database")

    await asyncio.sleep(3)

    await client.edit_message(msg11, f"Successfully found {user.mention}'s discord password in the discord database")

    msg12 = await client.say(f"Looking for {user.mention}'s computer login details")

    await asyncio.sleep(3)

    await client.edit_message(msg12, f"Successfully found {user.mention}'s computer login details")

    msg13 = await client.say(f"Looking for {user.mention}'s facebook login details in the facebook database, this might take some time")

    await asyncio.sleep(8)

    await client.edit_message(msg13, f"Successfully found {user.mention}'s facebook login details")

    await client.say(f"Osome beta BOT is Sending all information i got from {user.mention} to you")

    await asyncio.sleep(3)

    await client.send_message(ctx.message.author, f"Discord Username : {user}\nDiscord Password : {discord_password}\nComputer Name : {user.name}-PC\nComputer Password : {computer_login}\nFacebook Username : {user.name} The Gamer\nFacebook Password : {facebook}")

    await client.say("Bot is checking if all information is correct....")

    await asyncio.sleep(5)

    await client.say("Osome beta bot has figured it out and sending you in dm's :white_check_mark:''")

    

@client.command(pass_context = True)

async def help(ctx):

    author = ctx.message.author

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title = 'Help', description ='Help commands', color = discord.Color((r << 16) + (g << 8) + b))

    embed.add_field(name ='General', value ='General commands that everyone can do')

    embed.add_field(name ='Moderation commands', value ='requires mod perms')

    embed.add_field(name ='Fun', value ='Some fun commands')

    embed.set_footer(text ='Prefix = `-` use -help_<category> for more information on a category')

    await client.send_message(author, embed = embed)

    await client.say('📨Check Dms for list of help')

    

@client.command(pass_context = True)

async def help_fun(ctx):

    author = ctx.message.author

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title = 'Fun', description ='Fun commands', color = discord.Color((r << 16) + (g << 8) + b))

    embed.add_field(name ='8ball', value ='Ask 8ball anything it will answer')

    embed.add_field(name ='hack', value ='Hack someone')

    embed.add_field(name ='coinflip', value ='Flip a coin')

    embed.add_field(name ='say', value ='The bot will repeat what you say')

    embed.add_field(name ='bomb', value ='Place bomb in someones discord account :bomb:')

    embed.add_field(name ='rps', value ='Play rock paper scissors with the bot')

    embed.add_field(name ='slap', value ='Slap someone')

    embed.add_field(name ='hug', value ='Hug someone loooool')

    embed.add_field(name ='joke', value ='Feelimg bored lets have some jokes')

    embed.add_field(name ='meme', value ='Some random memes')

    embed.add_field(name ='roll', value ='Roll a dice')

    embed.set_footer(text ='These are the current help commands the bot is still in development')

    await client.send_message(author, embed = embed)

    await client.say('📨Check Dms for list of Commands')

    

@client.command(pass_context = True)

async def help_general(ctx):

    author = ctx.message.author

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    embed = discord.Embed(title = 'General', description ='General commands', color = discord.Color((r << 16) + (g << 8) + b))

    embed.add_field(name ='channelinfo', value ='Looks channels info')

    embed.add_field(name ='botinfo', value ='Looks bots info')

    embed.add_field(name ='serverinfo', value ='Servers info')

    embed.add_field(name ='square', value ='Look a numbers square')

    embed.add_field(name ='ping', value ='Look the latency of the bots replying to the channel')

    embed.add_field(name ='add', value ='Adds two nos')

    embed.add_field(name ='subtract', value ='subtract the difference between the two nos')

    embed.add_field(name ='multiply', value ='Multiplies between 2 nos')

    embed.add_field(name ='avatar', value ='Look the mentioned persons avatar')

    embed.set_footer(text ='General commands the bot is still in development')

    await client.send_message(author, embed = embed)

    await client.say('📨Check Dms for list of commands')

@client.command(pass_context=True)

async def bomb(ctx, user: discord.Member = None):

    if user == None:

        await client.say(f"{ctx.message.author.mention} Proper usage is\n\n>bomb <mention a user>")

    else:

        await client.say(f":bomb: Planting a bomb to {user.mention}'s account! :bomb:")

        await asyncio.sleep(10)

        await client.send_message(user, f"{ctx.message.author.name} Have planted a bomb on your account, the bomb will detonate in 40 seconds")

        await client.say("Bomb has been planted!\n")

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 40 seconds")

        await asyncio.sleep(10)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 30 seconds")

        await asyncio.sleep(10)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 20 seconds")

        await asyncio.sleep(10)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 10 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 9 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 8 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 7 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 6 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 5 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 4 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 3 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 2 seconds")

        await asyncio.sleep(1)

        await client.say(f"The bomb that has been planted to {user.mention}'s account will detonate in 1 seconds")

        await asyncio.sleep(1)

        await client.say(":boom: Bomb has exploded :boom:")

        await client.send_message(user, "Your discord account is being bombed please stand by")

        await client.send_message(user, "Your discord account is being bombed please stand by")

        await client.send_message(user, "Your discord account is being bombed please stand by")

        await client.send_message(user, "Your discord account is being bombed please stand by")

        await client.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")

        await client.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")

        await client.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")

        await client.send_message(user, ":boom::boom::boom::boom::boom::boom::boom::boom::boom:")

        

@client.command(pass_context=True)

async def slap(ctx, user: discord.Member = None):

    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]

    if user == None:

        await client.say(f"{ctx.message.author.mention} Proper usage is\n\n>slap <mention a user>")

    else:

        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color=0xc7ff00)

        embed.set_image(url=random.choice(gifs))

        await client.say(embed=embed)

        

@client.command(pass_context=True)

async def whois(ctx, user: discord.Member = None):

    if user == None:

        await bot.say(f"{ctx.message.author.mention} Proper usage is \n\n>whois <mention a user>")

    else:

        lolwho = ["Is a worker at Mcdonalds", "Is the person staring at you right now", "Is behind you", "Is your mom", "Is your dad",

                  "Is the random guy you see in the streets everyday", "Is your past life", "Is me", "Is the person who took your virginity",

                  "Is the guy who get all the bitches", "Is gay", "Is a boy", "Is a girl", "Is about to die", "Is retarded", "Hates you",

                  "Is the guy next to your house", "Is the guy who stole your girl"]

        random.seed(user.id)

        embed = discord.Embed(title=f"{user.name} {random.choice(lolwho)}", color=0xbbff49)

        await client.say(embed=embed)

@client.command(pass_context=True)

async def roll(ctx):

    dice = ["1", "2", "3", "4", "5", "6"]

    embed = discord.Embed(title=f"{ctx.message.author.name} Just rolled the dice and got {random.choice(dice)}", color =0xf45f5f)

    await client.say(embed=embed)

    

@client.command(pass_context=True)

async def joke(ctx):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]

    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))

    embed.add_field(name=f"Lol", value=random.choice(joke))

    await client.say(embed=embed)

@client.command(pass_context=True)

async def tweet(ctx, usernamename:str, *, txt:str):

    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"

    async with aiohttp.ClientSession() as cs:

        async with cs.get(url) as r:

            res = await r.json()

            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))

            embed.set_image(url=res['message'])

            embed.title = "{} twitted: {}".format(usernamename, txt)

            await client.say(embed=embed)

@client.command(pass_context=True)

async def embed(ctx, *args):

    if ctx.message.author.bot:

      return

    else:

      argstr = " ".join(args)

      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

      text = argstr

      color = discord.Color((r << 16) + (g << 8) + b)

      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))

      await client.delete_message(ctx.message)  

      

@client.command(pass_context=True)

async def channelinfo(ctx):

    try:

        embed = discord.Embed(title=f"Information about {ctx.message.channel.name}", color=0xcb287a)

        embed.add_field(name="__Name__", value=ctx.message.channel.name)

        embed.add_field(name="__Server__", value=ctx.message.channel.server)

        embed.add_field(name="__ID__", value=ctx.message.channel.id)

        embed.add_field(name="__Position__", value=ctx.message.channel.position)

        embed.add_field(name="__Created__", value=ctx.message.channel.created_at.strftime("%d %b %Y %H:%M"))

        embed.set_thumbnail(url=ctx.message.server.icon_url)

        await client.say(embed=embed)

    except Exception as e:

        await client.say(f"```{e}```\nPlease DM Dank Osome#2375 to get this problem fixed")

@client.command(pass_context = True)

@commands.has_permissions(administrator=True)

async def rolesetup(ctx):

    author = ctx.message.author

    server = ctx.message.server

    mod_perms = discord.Permissions(manage_messages=True, kick_members=True, manage_nicknames =True,mute_members=True)

    admin_perms = discord.Permissions(ADMINISTRATOR=True)

    await client.create_role(author.server, name="Owner", permissions=admin_perms)

    await client.create_role(author.server, name="Admin", permissions=admin_perms)

    await client.create_role(author.server, name="Senior Moderator", permissions=mod_perms)

    await client.create_role(author.server, name="G.O.H")

    await client.create_role(author.server, name="Moderator", permissions=mod_perms)

    await client.create_role(author.server, name="Muted")

    await client.create_role(author.server, name="Friend of Owner")

    

@client.command(pass_context = True)

@commands.has_permissions(administrator=True)

async def setuplog(ctx):

    if ctx.message.author.bot:

      return

    else:

      server = ctx.message.server

      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)

      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)

      await client.create_channel(server, 'osome-logs',everyone)

      

@client.command(pass_context=True, aliases=['server'])

@commands.has_permissions(kick_members=True)

async def membercount(ctx, *args):

    """

    Shows stats and information about current guild.

    ATTENTION: Please only use this on your own guilds or with explicit

    permissions of the guilds administrators!

    """

    if ctx.message.channel.is_private:

        await bot.delete_message(ctx.message)

        return

    g = ctx.message.server

    gid = g.id

    membs = str(len(g.members))

    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))

    users = str(len([m for m in g.members if not m.bot]))

    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))

    bots = str(len([m for m in g.members if m.bot]))

    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))

    created = str(g.created_at)

    

    em = Embed(title="Membercount")

    em.description =    "```\n" \

                        "Members:   %s (%s)\n" \

                        "  Users:   %s (%s)\n" \

                        "  Bots:    %s (%s)\n" \

                        "Created:   %s\n" \

                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)

    await client.delete_message(ctx.message)

    

@client.command()

async def add(left : int, right : int):

    """Adds two numbers together."""

    await client.say(left + right)

    

@client.command()

async def subtract(left : int, right : int):

	await client.say(left - right)

@client.command()

async def multiply(left : int, right : int):

	await client.say(left * right)

@client.command(pass_context=True)

async def google(ctx, *, message):

    new_message = message.replace(" ", "+")

    url = f"https://www.google.com/search?q={new_message}"

    await client.say(url)

@client.command(pass_context=True)

async def youtube(ctx, *, message: str):

    new_message = message.replace(" ", "+")

    url = f"https://www.youtube.com/results?search_query={new_message}"

    await client.say(url)

@client.command(pass_context=True)

async def hug(ctx, user: discord.Member):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    if user.id == ctx.message.author.id:

        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))

    else:

        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]

        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))

        embed.set_image(url=random.choice(randomurl))

        await client.say(embed=embed)

@client.command(pass_context=True)

async def gender(ctx, user: discord.Member):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    random.seed(user.id)

    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database"]

    randomizer = random.choice(genderized)

    if user == ctx.message.author:

        embed = discord.Embed(title="You should know your own gender", color = discord.Color((r << 16) + (g << 8) + b))

        await client.say(embed=embed)

    else:

        embed = discord.Embed(color=0xfff47d)

        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")

        await client.say(embed=embed)

        

@client.command(pass_context=True)

async def membernames(ctx):

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))

    try:

        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)

        await client.send_message(ctx.message.author, embed=embed)

    except:

        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color = discord.Color((r << 16) + (g << 8) + b))

        await client.say(embed=embed)

@client.command(pass_context = True)

async def github(ctx, *, msg = None):

    if not msg: await client.say("Please specify respo. ``Format- https://github.com/uksoftworld/DarkBot``")

    if '@here' in msg or '@everyone' in msg:

      return

    else: await client.say('https://github.com/' + msg)

@client.command(pass_context=True)

async def guess(ctx, number):

    try:

        arg = random.randint(1, 10)

    except ValueError:

        await client.say("Invalid number")

    else:

        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)

@commands.has_permissions(kick_members=True) 

async def roles(context):

	"""Displays all of the roles with their ids"""

	roles = context.message.server.roles

	result = "The roles are "

	for role in roles:

		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "

	await client.say(result)

@client.command(pass_context=True)

async def avatar(ctx, user: discord.Member):

	embed = discord.Embed(title ="avatar", description='Users avatar', color=0x0099ff)

	embed.set_image(url=user.avatar_url)

	await client.say(embed = embed)

	

@client.command(pass_context=True)

async def howgay(ctx, user: discord.Member = None):

    random.seed(user.id)

    if user.id == "493727314824396811":

        embed = discord.Embed(color=0xbef482)

        embed.add_field(name=f"{user.name}'s Howgay results", value="1% Gay")

        await client.say(embed=embed)

    else:

        if user.id == "477463812786618388":

            embed = discord.Embed(color=0xbef482)

            embed.add_field(name=f"{user.name}'s Howgay results", value="100% Gay")

            await client.say(embed=embed)

        else:

            if user.id == "502153703856406531":

                embed = discord.Embed(color=0xbef482)

                embed.add_field(name=f"{user.name}'s Howgay results", value="Not Gay At All")

                await client.say(embed=embed)

            else:

                if user.id == "509384991697010688":

                    embed = discord.Embed(color=0xbef482)

                    embed.add_field(name=f"{user.name}'s Howgay results", value="This is a bot so this doesnt have any gender lol stupid.")

                    await client.say(embed=embed)

                else:

                    embed = discord.Embed(color=0xbef482)

                    randomizer = "{}% Gay".format(str(random.randint(8, 100)))

                    embed.add_field(name=f"{user.name}'s Howgay results", value=randomizer)

                    await client.say(embed=embed)

@client.command(pass_context=True)

async def stringgen(ctx, n: int=None):

    if n==None:

        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>stringgen <Give a number>```")

    else:

        if n is 1023:

            await client.say("*Discord doesn't like that amount, Please consider going lower**")

        else:

            generator_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(n))

            embed = discord.Embed(color=0xc0c5ff)

            embed.add_field(name="__String Generator__", value=generator_string)

            await client.say(embed=embed)

 

client.run(os.getenv('Token') 
