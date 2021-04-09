# Mee6AutoXP bot
# Written by ef1500
#
# Mee6AutoXP.py

# Process: We want to use a lsit of base phrases to send in chat.
from discord.ext import commands
import asyncio
import discord
import random
import time

#Our discord token. We use this to run the bot from our own account.
token = "TOKEN"

#Channel ID of the channel you want to send messages to.
channel_id = CHANNEL_ID

client = commands.Bot(command_prefix = '>',case_insensitive=True)

#send a random phrase every few minutes
@client.listen()
async def on_message(message):
    time.sleep(1.25)
    phrases = open("phrases.txt", 'r')
    phrase_lst = [line.split(',') for line in phrases.readlines()]
    random_phrase = random.randrange(len(phrase_lst))
    message.channel_id.send(random_phrase)
    sleep_time = random.randint(60, 240) #anywhere from one minute to four minutes
    time.sleep(sleep_time)

    await client.process_commands(message)

client.run(token, bot=False)

# Best Regards,
#            ~ef1500
#           「私だけの犯罪が好奇心のそれ」
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
