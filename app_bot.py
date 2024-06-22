# app.py module
import logging
from database import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import *
from inline_button import keyboard

API_TOKEN = "5843003643:AAGHQTQJZ4A_WgV0zPdAMXrgnwA5net7CVU"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    # query = f"INSERT INTO bot(username, full_name, user_id) VALUES('{username}', '{full_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Botga hush kelibsiz : {first_name}", reply_markup=menu_keyboard)
    else:
        # await Database.connect(query, "insert")
        await message.reply(f"Assalomu alaykum :  {full_name}", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Menyu 💻")
async def show_menu_1(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer(" 💻 Menyulardan birini tanglang 💻 ", reply_markup=menu_leptop)

@dp.message_handler(lambda message: message.text == "MacBook Leptop 💻")
async def show_menu_2(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer(" MacBook kampyutirlari 💻 ", reply_markup=macbook)

@dp.message_handler(lambda message: message.text == "MacBook 💻")
async def show_menu_3(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer(" MacBook information 💻 ", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Back 🔙")
async def show_menu_4(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer(" Back ", reply_markup=menu_keyboard)

@dp.message_handler(lambda message: message.text == "Menyu 📱")
async def show_menu_5(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer(" 📱 Menyulardan birini tanglang 📱 ", reply_markup=menu_phone)


@dp.message_handler(lambda message: message.text == "Samsung 📱")
async def show_menu_6(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("  SAMSUNG telefonlarining ruyhati Samsung 📱", reply_markup=samsung)


@dp.message_handler(lambda message: message.text == "Iphone 📱")
async def show_menu_7(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer(" Apple Iphone telefonlarining ruyhati 📱", reply_markup=iphone)


@dp.message_handler()
async def echo_8(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
