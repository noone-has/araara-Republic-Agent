import discord
import save_data

async def handle(message: discord.Message, command, args):
    if(command == "reply"):
        await message.reply("Reply test")
    elif(command == "msgs"):
        await message.reply(save_data.update_msgs_sent(message.author.name))
