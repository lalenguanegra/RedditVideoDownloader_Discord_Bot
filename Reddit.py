import discord
import sys
import subprocess 
from subprocess import call
from discord.ext import commands
from pathlib import Path
bot = commands.Bot(command_prefix='!')

@bot.command()
async def red(ctx, arg):
    dest = Path('URL.py')
    src = Path('DEFAULT.txt')
    dest.write_bytes(src.read_bytes())
    dest.write_text(src.read_text())
    path = Path('URL.py')
    text = path.read_text()
    text = text.replace('http', arg)
    path.write_text(text)

@bot.command()
async def go(ctx):
    await ctx.send("Loading...")
    subprocess.call("URL.py", shell=True)
    await ctx.send("downloaded!")

@bot.command()
async def email(ctx):
    await ctx.send("Sending Email...")
    subprocess.call("Email_Video.py", shell=True)
    await ctx.send("SENT!")

@bot.command()
async def gone(ctx):
    await ctx.send("Deleted...")
    subprocess.call("DEL.py", shell=True)
bot.run('token')