
import os
import random
import asyncio
import discord

discord_token = input("Insert the discord token: ")


dclient = discord.Client()

walrus_list = [
    "<:walrus1:714931542602022984>",
    "<:walrus2:714932333500956753>",
    "<:walrus3:714932351964282920>",
    "<:walrus4:738498294367518721>",
    "<:walrus5:738498939887812691>"
]


@dclient.event
async def on_ready():
    print(f'{dclient.user} has connected to Discord')

    guild_dict = {g.name:g.id for g in dclient.guilds}

    print("You are connected to: ")
    print(guild_dict)


@dclient.event
async def on_message(message):
    if message.author != dclient.user:
        try:
            print(str(message.author).encode('utf-8'))
            rcvd_msg = str(message.content).encode('utf-8') # .decode('utf-8')
            print(rcvd_msg)
        except:
            print("parse error")

        if (str(message.author) == 'WalrusAir#1391'):
            for walrus in random.sample(walrus_list, random.randint(1,3) + random.randint(0,1)):
                await asyncio.sleep(random.uniform(0, 30) + random.uniform(0, 5))
                await message.add_reaction(walrus)


if __name__ == '__main__':
    dclient.run(discord_token)
