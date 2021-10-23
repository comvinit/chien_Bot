import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents = intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")
 
@bot.event
async def on_member_joun(member):
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')

bot.run('OTAxMjg4MTc2NjI1Mjc0OTAw.YXNsBg.mMs-rDoNAxTzj_cwKtSoSsNc10I')