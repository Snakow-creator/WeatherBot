from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главные кнопки
main = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Подробный прогноз")]],
    resize_keyboard=True,
    input_field_placeholder="Выберите список ниже:",
)
