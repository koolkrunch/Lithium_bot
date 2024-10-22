import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')
    await bot.change_presence(activity=discord.Game(name="in a Zoo"))

cogs_list = {
    'general'
}


for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(os.getenv('TOKEN'))