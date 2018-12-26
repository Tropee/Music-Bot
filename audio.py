import discord

@client.event
async def on_ready():
  print('Hi')
  
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Supporter')
    await client.add_roles(member, role)

bot.run(os.environ['BOT_TOKEN'])
