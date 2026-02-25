from pyrogram import Client
from pyrogram.types import Message

import config


bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="MY_BOT"
)


@bot.on_message()
async def echo(client: Client, message: Message):
    await message.reply(f"Я не знаю что это {message.text}. Попробуйте /help")

bot.run()
