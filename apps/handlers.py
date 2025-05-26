from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart

from parser.global_weather import get_gweather

import apps.keyboards as kb

router = Router()


class Weather(StatesGroup):
    Global = State()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Хей! Привет - я бот который определяет погоду силой мысли!",
        reply_markup=kb.main,
    )


@router.message(F.text == "Подробный прогноз")
async def full_weather(message: Message, state: FSMContext):
    await state.set_state(Weather.Global)
    await message.delete()
    await message.answer(
        "Точный и подробный прогноз погоды.\n\n"
        "Введите город (Важно! Вводите точное название города или населенного пункта):"
    )


@router.message(Weather.Global)
async def full_weather_state(message: Message, state: FSMContext):
    city = message.text
    await state.clear()
    await get_gweather(message=message, city=city)
