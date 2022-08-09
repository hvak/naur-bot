import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def naurify(ctx, arg):
    print(arg)
    await ctx.send(naur_translate(arg))


def naur_translate(msg):
    msg = msg.replace('a', 'ar')
    msg = msg.replace('oe', 'aur')
    msg = msg.replace('o', 'aur')

    return msg

#bot.add_command(naurify)

bot.run('<insert token>')
