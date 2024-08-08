from aiogram.types import Message
from loader import dp
from data.weather import get_weather_day

@dp.message(lambda message:message.text =="/bugun")
async def bugun_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.answer(get_weather_day())
        print(message)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")