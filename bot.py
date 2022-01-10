import os
from discord.ext import commands


TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


"""
Tenemos las siguientes redes sociales a compartir:
https://www.twitch.tv/ccoza94
https://youtube.com/channel/UC_R3FByDlsRGaDhP_tgqpgQ
https://twitter.com/ccoza94
https://www.instagram.com/ccozza_/
https://www.tiktok.com/@ccoza94
"""
@bot.command(name='redes', help='Comando para ver las redes sociales')
async def social_network(ctx):
    twitch = "- Twitch: https://www.twitch.tv/ccoza94"
    youtube = "- YouTube: https://youtube.com/channel/UC_R3FByDlsRGaDhP_tgqpgQ"
    twitter = "- Twitter: https://twitter.com/ccoza94"
    instagram = "- Instagram: https://www.instagram.com/ccozza_/"
    tiktok = "- TikTok: https://www.tiktok.com/@ccoza94"

    response = f"👾 Sigueme en mis redes sociales! 👾\n  {twitch}\n {youtube}\n {twitter}\n {instagram}\n {tiktok}"
    await ctx.send(response)


# Command whit arguments
# @bot.command(name='roll_dice', help='Simulates rolling dice.')
# async def roll(ctx, number_of_dice: int, number_of_sides: int):
#     dice = [
#         str(random.choice(range(1, number_of_sides + 1)))
#         for _ in range(number_of_dice)
#     ]
#     await ctx.send(', '.join(dice))


bot.run(TOKEN)
