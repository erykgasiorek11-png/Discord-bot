import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name} (ID: {bot.user.id})')
    print('Bot jest gotowy do działania!')

@bot.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if channel.name in ['powitania', 'witajcie', 'general']:
            await channel.send(f'Cześć {member.mention}! Witaj na serwerze **{member.guild.name}**! 🎉')
            break

@bot.command(name='ping')
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Opóźnienie wynosi: {latency}ms')

@bot.command(name='czysc', help='Usuwa określoną liczbę wiadomości z kanału.')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'Usunięto {amount} wiadomości.', delete_after=3)

bot.run('TWÓJ_TOKEN_BOTA')
