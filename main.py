import discord.ext.commands as commands
import discord
import random
import json
import os
import requests

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is ready!")


# Add a insult command that sends a GET request to https://evilinsult.com/generate_insult.php?lang=en&type=json to get a random insult.
@bot.command()
async def insult(ctx, user: discord.User):
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    data = response.json()
    mention = user.display_name
    embed = discord.Embed(title="Insult for "+mention, description=mention + ", "+ data["insult"], color=0x00ff00)
    await ctx.send(embed=embed)
# Add a rickroll command
@bot.command()
async def rickroll(ctx):
    await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# Add a ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
# Add a command to get the account information of a user
@bot.command()
async def account_info(ctx, user: discord.User):
    embed = discord.Embed(title="Account Info", description="Information about the account", color=0x00ff00)
    embed.add_field(name="Username", value=user.name, inline=False)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(name="Created At", value=user.created_at, inline=False)
    await ctx.send(embed=embed)
# Add a command to get the server infromation of a server
@bot.command()
async def server_info(ctx, server: discord.Guild):
    embed = discord.Embed(title="Server Info", description="Information about the server", color=0x00ff00)
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="ID", value=server.id, inline=False)
    embed.add_field(name="Created At", value=server.created_at, inline=False)
    await ctx.send(embed=embed)
# Add a command to get the role infromation of a role
@bot.command()
async def role_info(ctx, role: discord.Role):
    embed = discord.Embed(title="Role Info", description="Information about the role", color=0x00ff00)
    embed.add_field(name="Name", value=role.name, inline=False)
    embed.add_field(name="ID", value=role.id, inline=False)
    embed.add_field(name="Created At", value=role.created_at, inline=False)
    await ctx.send(embed=embed)
# Add a command to get the channel infromation of a channel
@bot.command()
async def channel_info(ctx, channel: discord.TextChannel):
    embed = discord.Embed(title="Channel Info", description="Information about the channel", color=0x00ff00)
    embed.add_field(name="Name", value=channel.name, inline=False)
    embed.add_field(name="ID", value=channel.id, inline=False)
    embed.add_field(name="Created At", value=channel.created_at, inline=False)
    await ctx.send(embed=embed)

# Add a joke command and send a GET request to https://api.chucknorris.io/jokes/random to get a random joke from the API
@bot.command()
async def joke(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    embed = discord.Embed(title="Joke", description=data["value"], color=0x00ff00)
    await ctx.send(embed=embed)

# Add a command to get the bot version
@bot.command()
async def version(ctx):
    embed = discord.Embed(title="Version", description="Development version 0.1", color=0x00ff00)
    await ctx.send(embed=embed)

# Add a command to get the source of the bot
@bot.command()
async def source(ctx):
    embed = discord.Embed(title="Source", description="You want the source, huh? Alright FINE its at import discord.ext.commands as commands
import discord
import random
import json
import os
import requests

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is ready!")


# Add a insult command that sends a GET request to https://evilinsult.com/generate_insult.php?lang=en&type=json to get a random insult.
@bot.command()
async def insult(ctx, user: discord.User):
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    data = response.json()
    mention = user.display_name
    embed = discord.Embed(title="Insult for "+mention, description=mention + ", "+ data["insult"], color=0x00ff00)
    await ctx.send(embed=embed)
# Add a rickroll command
@bot.command()
async def rickroll(ctx):
    await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# Add a ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
# Add a command to get the account information of a user
@bot.command()
async def account_info(ctx, user: discord.User):
    embed = discord.Embed(title="Account Info", description="Information about the account", color=0x00ff00)
    embed.add_field(name="Username", value=user.name, inline=False)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(name="Created At", value=user.created_at, inline=False)
    await ctx.send(embed=embed)
# Add a command to get the server infromation of a server
@bot.command()
async def server_info(ctx, server: discord.Guild):
    embed = discord.Embed(title="Server Info", description="Information about the server", color=0x00ff00)
    embed.add_field(name="Name", value=server.name, inline=False)
    embed.add_field(name="ID", value=server.id, inline=False)
    embed.add_field(name="Created At", value=server.created_at, inline=False)
    await ctx.send(embed=embed)
# Add a command to get the role infromation of a role
@bot.command()
async def role_info(ctx, role: discord.Role):
    embed = discord.Embed(title="Role Info", description="Information about the role", color=0x00ff00)
    embed.add_field(name="Name", value=role.name, inline=False)
    embed.add_field(name="ID", value=role.id, inline=False)
    embed.add_field(name="Created At", value=role.created_at, inline=False)
    await ctx.send(embed=embed)
# Add a command to get the channel infromation of a channel
@bot.command()
async def channel_info(ctx, channel: discord.TextChannel):
    embed = discord.Embed(title="Channel Info", description="Information about the channel", color=0x00ff00)
    embed.add_field(name="Name", value=channel.name, inline=False)
    embed.add_field(name="ID", value=channel.id, inline=False)
    embed.add_field(name="Created At", value=channel.created_at, inline=False)
    await ctx.send(embed=embed)

# Add a joke command and send a GET request to https://api.chucknorris.io/jokes/random to get a random joke from the API
@bot.command()
async def joke(ctx):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    embed = discord.Embed(title="Joke", description=data["value"], color=0x00ff00)
    await ctx.send(embed=embed)

# Add a command to get the bot version
@bot.command()
async def version(ctx):
    embed = discord.Embed(title="Version", description="Development version 0.1", color=0x00ff00)
    await ctx.send(embed=embed)

# Add a command to get the source of the bot
@bot.command()
async def source(ctx):
    embed = discord.Embed(title="Source", description="You want the source, huh? Alright FINE its at https://github.com/Erix-glitch/insultbot", color=0x00ff00)
    await ctx.send(embed=embed)

# Add a help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="List of commands", color=0x00ff00)
    embed.add_field(name="!insult @user", value="Sends a random insult to the user", inline=False)
    embed.add_field(name="!rickroll", value="Sends a random rickroll", inline=False)
    embed.add_field(name="!ping", value="Sends a ping", inline=False)
    embed.add_field(name="!account_info @user", value="Sends account information of the user", inline=False)
    embed.add_field(name="!server_info @server", value="Sends server information of the server", inline=False)
    embed.add_field(name="!role_info @role", value="Sends role information of the role", inline=False)
    embed.add_field(name="!channel_info @channel", value="Sends channel information of the channel", inline=False)
    embed.add_field(name="!joke", value="Sends a random joke", inline=False)
    embed.add_field(name="!source", value="Sends the source of the bot", inline=False)
    await ctx.send(embed=embed)

# Add a help command
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="List of commands", color=0x00ff00)
    embed.add_field(name="!insult @user", value="Sends a random insult to the user", inline=False)
    embed.add_field(name="!rickroll", value="Sends a random rickroll", inline=False)
    embed.add_field(name="!ping", value="Sends a ping", inline=False)
    embed.add_field(name="!account_info @user", value="Sends account information of the user", inline=False)
    embed.add_field(name="!server_info @server", value="Sends server information of the server", inline=False)
    embed.add_field(name="!role_info @role", value="Sends role information of the role", inline=False)
    embed.add_field(name="!channel_info @channel", value="Sends channel information of the channel", inline=False)
    embed.add_field(name="!joke", value="Sends a random joke", inline=False)
    embed.add_field(name="!source", value="Sends the source of the bot", inline=False)
    await ctx.send(embed=embed)
bot.run('token')
