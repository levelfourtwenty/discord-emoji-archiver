import discord
import requests
import os

bot = discord.Client(self_bot=True)

token = "YOUR TOKEN HERE"


@bot.event
async def on_ready():
        print("ready")



@bot.event
async def on_message(message):
        if message.content == "YOUR SECRET STRING HERE":
                await message.delete()
                dirname = message.guild.name
                dirname = dirname.replace(" ", "_")
                os.mkdir(dirname)
                totallength = len(message.guild.emojis)
                currentemoji = 0
                for i in message.guild.emojis:
                        currentemoji += 1
                        print(f"Downloading {i.name}...")
                        req = requests.get(i.url)
                        match i.animated:
                                case True:
                                        open(f"{dirname}/{i.name}.gif", "wb").write(req.content)
                                case False:
                                        open(f"{dirname}/{i.name}.png", "wb").write(req.content)
                        print(f"Finished downloading {i.name} [{currentemoji}/{totallength}].\n")


bot.run(token, bot=False)
