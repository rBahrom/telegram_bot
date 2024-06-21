from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("Menyu 💻"), KeyboardButton("Menyu 📱")]
],
    resize_keyboard=True)


menu_leptop = ReplyKeyboardMarkup([
    [KeyboardButton("MacBook M2 Pro 💻"), KeyboardButton("Hp 💻")],
    [KeyboardButton("Acer 💻"), KeyboardButton("Lenovo 💻")],
    [KeyboardButton("Asus 💻"), KeyboardButton(" AIO 💻")],
    [KeyboardButton("Back 🔙")]
],
    resize_keyboard=True)

macbook = ReplyKeyboardMarkup([
    [KeyboardButton("MacBook  💻"), KeyboardButton("MacBook Pro 💻")],
    [KeyboardButton("MacBook M1 💻"), KeyboardButton("MacBook M1 Pro 💻")],
    [KeyboardButton("MacBook M2 💻"), KeyboardButton(" MacBook M2 Pro 💻")],
    [KeyboardButton("Buy")],
    [KeyboardButton("Back 🔙")]
],
    resize_keyboard=True)

menu_phone = ReplyKeyboardMarkup([
    [KeyboardButton("Samsung 📱"), KeyboardButton("Iphone 📱 ")],
    [KeyboardButton("Redmi 📱"), KeyboardButton("Mi 📱")],
    [KeyboardButton("Poco 📱"), KeyboardButton(" Honor 📱")],
    [KeyboardButton("Back 🔙")]
],
    resize_keyboard=True)

samsung = ReplyKeyboardMarkup([
    [KeyboardButton("Samsung A 52 📱"), KeyboardButton("Samsung S20 ")],
    [KeyboardButton("Samsung S21 📱 "), KeyboardButton("Samsung S22 📱")],
    [KeyboardButton("Samsung Note 10 📱 "), KeyboardButton("Samsung Note 20 📱")],
[KeyboardButton("Buy")],
    [KeyboardButton("Back 🔙")]
],
    resize_keyboard=True)

iphone = ReplyKeyboardMarkup([
    [KeyboardButton("Iphone 13 📱"), KeyboardButton("Iphone 13 Pro 📱 ")],
    [KeyboardButton("Iphone 14 📱 "), KeyboardButton("Iphone 14 Pro 📱")],
    [KeyboardButton("Iphone 15 📱 "), KeyboardButton("Iphone 15 Pro 📱")],
    [KeyboardButton("Buy")],
    [KeyboardButton("Back 🔙")]
],
    resize_keyboard=True)

# addresses_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# addresses_keyboard.add(KeyboardButton("1"))
# addresses_keyboard.add(KeyboardButton("2"))
# addresses_keyboard.add(KeyboardButton("Back"))
#
