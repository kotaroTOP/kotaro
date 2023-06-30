import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('хай'):
        await message.channel.send("привет я кот программист развлекательный и помогающий чат бот ")
    elif message.content.startswith('посоветуй исполителя музыки'):
        await message.channel.send("RADIO TAPOK")
    elif message.content.startswith('посоветуй музыку для игр'):
        await message.channel.send("ночные ведьмы by RADIO TAPOK, capybara phonk, удали меня by wicsur")
    elif message.content.startswith('самое большое по просмотрам видео на ютубе'):
        await message.channel.send("АКУЛЁНОК Я ТУРУРУ")
client.run('token')
