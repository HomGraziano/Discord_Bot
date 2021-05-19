import discord
import random
from discord.ext import commands
token = "ODA2OTY2NjE3NjA2OTc5Njc0.YBxIOg.GgICqFTyEiU7yO29uPay9V_ztXY"
bot = commands.Bot(command_prefix='-')

@bot.command()
async def repo(ctx):
    await ctx.send('Mods Tecnicos: El "core" de funciones que usamos en las partidas (salto, mapa, ace, etc.): https://steamcommunity.com/sharedfiles/filedetails/?id=2118328177')
    await ctx.send('Mods Esteticos: Unifromes, chalecos, vehiculos, mapas, etc. que el editor necesite. https://steamcommunity.com/sharedfiles/filedetails/?id=2297260271')
    await ctx.send('Mejoras de audio: Pack de chimi visual hecho por @Kaleb: https://steamcommunity.com/sharedfiles/filedetails/?id=2127993737')

@bot.command()
async def contact(ctx):
    coord = ['south', 'north', 'east', 'west', 'front', 'left', 'right']
    dist = ['300', '200', '100', '400', '500', '600', '700', '800']
    tipo = ['Tank', 'Man', 'Sniper', 'Anti-tank', 'Unknown contact', 'Towelhead', 'Unknown waifu']
    p1 = random.choice(coord)
    p2 = random.choice(dist)
    p3 = random.choice(tipo)
    await ctx.send(f"{p3}! {p2} meters, {p1}.")

async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

bot.run(token)

