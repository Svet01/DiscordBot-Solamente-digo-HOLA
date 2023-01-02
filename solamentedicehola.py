from discord import app_commands, Intents, Client, Interaction
import os
import environ
import requests
from bs4 import BeautifulSoup



#Environ load and token
environ.Env.read_env()
TOKEN = os.environ['TOKEN']

class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
 
    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)
 
 
bot = Bot(intents=Intents.default())

@bot.tree.command()
async def valordolar(interaction: Interaction):
    # Hacer la solicitud HTTP a la página y obtener el contenido
    page = requests.get("https://dolarhoy.com/")
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Extraer el dato de la página usando BeautifulSoup
    venta_div = soup.find(class_="venta")
    valor_dolar = venta_div.find_all(class_="val")[0].text
    
    # Enviar un mensaje a Discord con el valor del dólar
    await interaction.response.send_message(f"El valor del dólar es {valor_dolar}")


@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")
 
@bot.tree.command()
async def canjearinsignia(interaction: Interaction):
    await interaction.response.send_message("Espera 24 horas para reclamar la insignia\nPuedes reclamarla aquí: https://discord.com/developers/active-developer")

@bot.tree.command()
async def holamundo(interaction: Interaction):
    await interaction.response.send_message("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA MUNDOOOOOOOOOOOOOOOOOOO")

@bot.tree.command()
async def hola(interaction: Interaction):
    await interaction.response.send_message("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


bot.run(TOKEN)
