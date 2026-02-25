import asyncio
import sys
from pyrogram import Client
from pyrogram.types import Message

import config

# СОЗДАЕМ ЦИКЛ СОБЫТИЙ ДЛЯ PYTHON 3.14
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="MY_BOT"
)

@bot.on_message()
async def echo(client: Client, message: Message):
    await message.reply(f"Я не знаю что это {message.text}. Попробуйте /help")

async def main():
    """Асинхронная функция запуска бота"""
    print("🚀 Запуск бота...")
    await bot.start()
    print("✅ Бот успешно запущен!")
    # Бесконечное ожидание
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    try:
        # Запускаем главную функцию в существующем цикле
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("👋 Бот остановлен")
    finally:
        # Корректно закрываем бота
        loop.run_until_complete(bot.stop())
