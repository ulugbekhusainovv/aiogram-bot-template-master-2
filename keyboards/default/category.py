from aiogram.types import  ReplyKeyboardMarkup , KeyboardButton

home = ReplyKeyboardMarkup(
    row_width=2
)

item1 = KeyboardButton(text="Home")
item2 = KeyboardButton(text="Categories")
item3 = KeyboardButton(text="Contact")
item4 = KeyboardButton(text="About")
home.add(item1, item2,item3, item4)