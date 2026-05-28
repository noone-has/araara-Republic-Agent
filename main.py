import get_token
import discord
import message_handler
import save_data

COMMAND_PREFIX = "!"

class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if(message.author == client.user):
            return

        save_data.update_msgs_sent(message.author.name)

        print(f'Message from {message.author}: {message.content}')
        if(message.content.startswith(COMMAND_PREFIX)):
            without_prefix = message.content.split(COMMAND_PREFIX)
            args = without_prefix[1].split(" ")
            command = args.pop(0)
            await message_handler.handle(message, command, args)

intents = discord.Intents.default()
intents.message_content = True

client = Bot(intents=intents)
client.run(get_token.read_or_write_token())