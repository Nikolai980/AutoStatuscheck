import os
import discord
from discord.ext import tasks, commands

TOKEN =  os.getenv("TOKEN")

bot = commands.Bot(
    command_prefix='-',
    intents = discord.Intents.all()
    )

# == Variable interval ==
guild_id = 878060638432280586#guild id
status_keyword = '.gg/zap'#The status keyword
role_id = 878064557229215754#The role id
# =======================

@tasks.loop(seconds = 2)
async def statusCheck():
    guild = bot.get_guild(guild_id)
    role = guild.get_role(role_id)
    for member in guild.members:
        if status_keyword in str(member.activity) and not role in member.roles:
            try: await member.add_roles(role)
            except: print(f'Try to give {member.name} role, but fail')
        elif status_keyword not in str(member.activity) and role in member.roles:
            try: await member.remove_roles(role)
            except: print(f'Try to give {member.name} role, but fail')


@bot.event
async def on_ready():
    print('bot is ready')
    statusCheck.start() 

bot.run(TOKEN)    
