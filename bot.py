import discord
from passgen import gen_pass, random_emoji
# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$genpass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emoji'):
        await message.channel.send(random_emoji())
    else:
        await message.channel.send(message.content)
client.run("")
