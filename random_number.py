import asyncio
from datetime import datetime

import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nummer(self, ctx):  # Zufallszahl zwischen 1 und 1000
        mess = await ctx.send('Deine Zufallszahl wird generiert!')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! .')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! ..')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! ...')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert!')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! .')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! ..')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! ...')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert!')
        await asyncio.sleep(0.51)
        await mess.edit(content='Deine Zufallszahl wird generiert! .')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! ..')
        await asyncio.sleep(0.5)
        await mess.edit(content='Deine Zufallszahl wird generiert! ...')
        await asyncio.sleep(3)
        await mess.edit(content='Deine Zufallszahl ist ``{}``'.format(random.randint(1, 1000)))


def setup(bot):
    bot.add_cog(Commands(bot))
