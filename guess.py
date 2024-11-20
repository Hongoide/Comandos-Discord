import discord, audioop, random as r, asyncio

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)
token = ""

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.event
async def on_message(message):
    # Evita que el bot se responda a sí mismo
    if message.author == bot.user:
        return

    if message.content.startswith('$guess'):
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = r.randint(1, 10)

        try:
            guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}.')
    
    # Asegúrate de procesar otros comandos
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run(token)
