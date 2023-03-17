from discord.ext import commands
import json
import discord
import asyncio


#intents setting
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

with open('item.json', "r", encoding="utf8") as file:
    data = json.load(file)


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.event
async def on_message(message):
    if message.channel == bot.get_channel(1086095100792279073):
        with open("message.txt","w") as message_file:
            message_file.write(message.content)
#        print(message.content)

bot.run(data['token'])

