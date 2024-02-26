import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {client.user}')

@client.event
async def on_message(message):
    #if message.author == client.user:
        #return
    if message.content.startswith('хай'):
        await message.channel.send("привет я ренгоку развлекательный дискорд чат бот!")
    elif message.content.startswith('дать печеньку'):
        await message.channel.send("ВКУСНО!")
   # else:
        #await message.channel.send(message.content)

client.run("token")
