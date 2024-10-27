import random
import discord
from discord.ext import commands

bot = discord.Bot()


class General(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @discord.slash_command(name='fish', description='Go fishing!')
    async def wave(self, ctx: discord.ApplicationContext):
        if random.randint(0, 10) == random.randint(0, 10):
            await ctx.respond('You Caught a fish!')
        else: await ctx.respond('No fish took the bait...')
        
    @discord.slash_command(name='d6', description='Roll a dice 1-6')
    async def d6(self, ctx: discord.ApplicationContext):
        rolled = random.randint(1, 6)
        await ctx.respond(f'You rolled a {rolled}')

    @discord.slash_command(name='d20', description='Roll a D20 (Die)')
    async def d20(self, ctx: discord.ApplicationContext):
        rolled = random.randint(1, 20)
        await ctx.respond(f'You rolled a {rolled}')

    @discord.slash_command(name='ping', description='See the latency of the bot.')
    async def ping(self, ctx: discord.ApplicationContext):
        await ctx.respond(f'Latency at {bot.latency}')
        

def setup(bot:commands.Bot):
    bot.add_cog(General(bot))