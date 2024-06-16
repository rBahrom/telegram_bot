# app.py module
import logging
from database import Database
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "5843003643:AAFDq-UhdnQluIuMwGm2EaMSljEbwqe0wwM"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO bot(username, full_name, user_id) VALUES('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Botga tashrifingiz uchun rahmat @{full_name}")
    else:
        await Database.connect(query, "insert")
        await message.reply(f"Assalomu alaykum @{full_name}")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
