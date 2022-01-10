import os
from discord.ext import commands


TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!", description="Estos son los comandos que hay disponibles")


# Social Media
twitch = "- Twitch: https://www.twitch.tv/ccoza94"
youtube = "- YouTube: https://youtube.com/channel/UC_R3FByDlsRGaDhP_tgqpgQ"
twitter = "- Twitter: https://twitter.com/ccoza94"
instagram = "- Instagram: https://www.instagram.com/ccozza_/"
tiktok = "- TikTok: https://www.tiktok.com/@ccoza94"


# Init Message
@bot.event
async def on_ready():
    print(f'{bot.user.name} se ha conectado a Discord!')


#
# Commands
##
@bot.command(name='redes', help='Comando para compartir las redes sociales en Discord')
async def social_network(ctx):
    response = f"🚀 Sigueme en mis redes sociales! 🚀\n {twitch}\n {youtube}\n {twitter}\n {instagram}\n {tiktok}\n"
    await ctx.send(response)


@bot.command(name='twitch', help='Comando para compartir el perfil de Twitch')
async def twitch_command(ctx):
    response = f"📲 {twitch}"
    await ctx.send(response)


@bot.command(name='youtube', help='Comando para compartir el perfil de YouTube')
async def youtube_command(ctx):
    response = f"📲 {youtube}"
    await ctx.send(response)


@bot.command(name='twitter', help='Comando para compartir el perfil de Twitter')
async def twitter_command(ctx):
    response = f"📲 {twitter}"
    await ctx.send(response)


@bot.command(name='instagram', help='Comando para compartir el perfil de Instagram')
async def instagram_command(ctx):
    response = f"📲 {instagram}"
    await ctx.send(response)


@bot.command(name='tiktok', help='Comando para compartir el perfil de TikTok')
async def tiktok_command(ctx):
    response = f"📲 {tiktok}"
    await ctx.send(response)


# Init Bot
bot.run(TOKEN)
