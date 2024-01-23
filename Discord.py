import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the token using the environment variable
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='intro')
async def intro(ctx):
    await ctx.send('Hello my master, I am Sidi, I am here to serve you as your slave, here is some information about me. I am black(inferior), I am gay and I am ready to serve you as the black dirty nigger lgbt I am.')

@bot.event
async def on_member_join(member):
    welcome_channel = member.guild.get_channel(1194057800012275792)
    await welcome_channel.send(f'Hey sir, {member.mention}! I am a dirty nigger: Please use !intro to learn more about me.')

@bot.command(name='verify')
async def verify(ctx):
    if isinstance(ctx.channel, discord.DMChannel):

        # Add a role to the user after verification
        verified_role = discord.utils.get(ctx.guild.roles, name='Member')
        await ctx.author.add_roles(verified_role)

        # Send a confirmation message
        await ctx.send('Verification successful! You now have access to the server.')

bot.run(DISCORD_TOKEN)
