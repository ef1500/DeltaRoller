# Auto-Mudae v1.0 by ef1500
#
# Commands:
# >自耕 - Will start rolling in hopes of getting a kakera reaction
# >妻 - Will start rolling in hopes of getting a character you want.
# NOTE: This bot will auto-snipe the characters you want as they pass
# by in the chat.
#
# TODO: FULL-AUTONOMOUS MODE
#       AUTO DK
#       AUTO MARRY/DIVORCE (KAKERA FARMING METHOD)
#       AUTO ROLL
#       MULTIPLE USER ACCOUNT CONTROL

from discord.ext import commands
import asyncio
import discord
import time
import re

#User Id of mudae
mudae_id = ID_OF_MUDAE

#User ID of ourselves
usr_id = YOUR_USER_ID

#Our discord token. We use this to run the bot from our own account.
token = "TOKEN"

#time to wait in between commands (in seconds)
timeout = 3

# Kakera Farming Command. This is the command that we will use to farm kakera.
#It should be the oppisite of the waifu farm command.
k_cmd = "$h"

#Waifu Farming command. We will use this to farm waifus.
w_cmd = "$wa"

client = commands.Bot(command_prefix = '>',case_insensitive=True)

# Listen for Kakera Emojis so we can farm them
@client.listen()
async def on_reaction_add(reaction, user):
    if reaction.message.author.id == mudae_id:
        msg = reaction.message
        if 'kakera' in str(reaction.emoji):
            await msg.add_reaction(emoji=reaction.emoji)

#listen for a message from mudae
@client.listen()
async def on_message(message):
    waifile = open("waifu.txt", 'r')
    waifu = [line.split(',') for line in waifile.readlines()]
    if message.author.id != mudae_id: #Check if author is mudae
        return
    for anime_girl in waifu:
        ax = str(anime_girl)
        ax2 = re.sub(r'([\[\]\/\{\}\.\,\']|(\\n))+', ' ', ax)
        ax2 = ax2.strip()
        for embed in message.embeds:
            if ax2 in str(embed.author):
                await message.add_reaction('❤️') #❤️ emoji

    await client.process_commands(message)

# Farming Mode (Kakera Farming with the "Sheer luck" method)
@client.listen()
async def on_message(message):
    if message.content == ">自耕":
        if message.author.id == usr_id:
            x=0
            while x < 10:
                await message.channel.send(k_cmd)
                time.sleep(timeout)
                x+=1
    await client.process_commands(message)

# Waifu Farming Mode
@client.listen()
async def on_message(message):
    if message.content == ">妻":
        if message.author.id == usr_id:
            x=0
            while x < 10:
                await message.channel.send(w_cmd)
                time.sleep(timeout)
                x+=1
    await client.process_commands(message)

client.run(token, bot=False)

# Best Regards,
#            ~ef1500
#
#             :*******************
#             :M$$MV***********V$M
#               *N$I*          :IF
#                 VN$M*
#                  :V$$I*
#                    *I$$F:
#                      *M$$V           :VFVV*
#                      :VF*:            *VVN$M:
#                    *VV*                  :M$M:
#                 :*V*:                     *N$I:
#               :VV*            :V:          V$$F:
#             *FV*::::::::::::::V$*         V$NN$F:
#            *$$$$$$$$$$$$$$$$$$$$*        *$N**$$V
#             ::::::::::::::::::::        *$N*  V$$*
#                                        *N$*    V$N*
#                                       *$N*      V$N*
#                                      *N$*        F$N*
#                                      :*:          ***
