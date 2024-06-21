from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="MacBook 95% ", callback_data="option1")
button2 = InlineKeyboardButton(text="MacBook 86%", callback_data="option2")
keyboard.add(button1, button2)
