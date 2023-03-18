from discord.ext import commands
import json
import discord
import asyncio
import re


#tell between the url and pure text message and seperate them
def separattion(x):
    url_test_sample = re.compile(r'http[s]?://\S+')
    url_match = url_test_sample.search(x)
    if url_match:
        url = url_match.group(0)
        text = x.replace(url, '').strip()
    else:
        url = None
        text = x
    file_writing(url, text)

def file_writing(input_url, input_text):
    #print(f"{input_url} {input_text}")
    with open("message.txt", "w") as message_file:
        message_file.write(input_url+input_text)


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
        separattion(message.content)


#        print(message.content)


bot.run(data['token'])

