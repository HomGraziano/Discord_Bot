import discord
import random
from discord.ext import commands
from config.config import TOKEN

class MyContext(commands.Context):
    async def tick(self, value):
        emoji = '\N{NAUSEATED FACE}' if value else '\N{CROSS MARK}'
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass
    
    async def contact(self, ctx):
        coord = ['south', 'north', 'east', 'west', 'front', 'left', 'right']
        dist = ['300', '200', '100', '400', '500', '600', '700', '800']
        tipo = ['Tank', 'Man', 'Sniper', 'Anti-tank', 'Unknown contact', 'Towelhead', 'Unknown waifu']
        await ctx.send(f"{random.choice(tipo)}! {random.choice(dist)} meters, {random.choice(coord)}.")
    
    async def repo(self, ctx):
        m1 = 'Mods Tecnicos: El "core" de funciones que usamos en las partidas (salto, mapa, ace, etc.): https://steamcommunity.com/sharedfiles/filedetails/?id=2118328177'
        m2 = 'Mods Esteticos: Uniformes, chalecos, vehiculos, mapas, etc. que el editor necesite. https://steamcommunity.com/sharedfiles/filedetails/?id=2297260271'
        m3 = 'Mejoras de audio: Pack de chimi visual hecho por @Kaleb: https://steamcommunity.com/sharedfiles/filedetails/?id=2127993737'
        await ctx.send(f'{m1} \n \n {m2} \n \n {m3}')

class MyBot(commands.Bot):
    async def get_context(self, message, *, cls=MyContext):
        return await super().get_context(message, cls=cls)
        
bot = MyBot(command_prefix='!')

@bot.command()
async def guess(ctx, number: int):
    value = random.randint(1, 2)
    await ctx.tick(number == value)


@bot.command()
async def contact(ctx, name = "bot"):
    await ctx.contact(ctx)

@bot.command()
async def repo(ctx):
    await ctx.repo(ctx)

bot.run(TOKEN)
