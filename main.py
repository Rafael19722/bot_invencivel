import discord
from discord import app_commands
import nest_asyncio
from discord.ext import commands
import asyncio

nest_asyncio.apply()

class Invencivel(discord.Client):
  def __init__(self):
    intents = discord.Intents.all()
    super().__init__(
        command_prefix="$",
        intents=intents
    )
    self.tree = app_commands.CommandTree(self)

  async def setup_hook(self):
    await self.tree.sync()

  async def on_ready(self):
    print(f"O bot {self.user} foi ligado com sucesso.")

bot = Invencivel()

@bot.event
async def on_message(message):
    # Evita que o bot responda a si mesmo
    if message.author == bot.user:
        return

    # Detectar a palavra na mensagem e responder com a imagem
    if any(word in message.content.lower() for word in ['intocavel', 'intocável', 'Intocável', 'Intocavel']):  # Verifica se a palavra está na mensagem
        # Enviar imagem relacionada a palavra
        await message.channel.send(embed=discord.Embed().set_image(url="https://media.discordapp.net/attachments/1348434998776303707/1355018617179213929/INTOCAVEL.jpg?ex=67e766ed&is=67e6156d&hm=40cea7059d130a0eb3abc546ca7463b284084087fed3a49e4d729426a66754a7&=&format=webp&width=814&height=576"))

    elif any(word in message.content.lower() for word in ['inrestringíve', 'Inrestringíve', 'Inrestringive', 'inrestringive', 'irrestringível', 'irrestringivel']):
        await message.channel.send(embed=discord.Embed().set_image(url="https://media.discordapp.net/attachments/1348434954337652797/1355019410414375003/image.png?ex=67e767aa&is=67e6162a&hm=810e9340d3f7948dac104cfa9184a387eab47a5cd55fbc5a777d620627d36f13&=&format=webp&quality=lossless"))

    elif any(word in message.content.lower() for word in ['indefinível', 'Indefinível', 'Indefinivel', 'indefinivel']):
        await message.channel.send(embed=discord.Embed().set_image(url="https://media.discordapp.net/attachments/1348434976571527259/1355018828882509935/indefinivel_true.jpg?ex=67e7671f&is=67e6159f&hm=d644bfa2edbb0c8ca534be74c263f5f941952f57f53b4a8a4515b252833eb7a8&=&format=webp&width=814&height=576"))

async def run_bot():
    await bot.start("###")


asyncio.run(run_bot())

