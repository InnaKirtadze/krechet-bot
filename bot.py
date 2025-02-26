from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio

TOKEN = "7696699237:AAGjeU5_tetHUGIbldfnE3d-GeZ6bx-URqw"
bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✨ Про мене й не тільки", url="https://t.me/krechetirina")],
        [InlineKeyboardButton(text="📞 Консультації", url="https://t.me/krechetirina")],
        [InlineKeyboardButton(text="📝 Записатися на консультацію", url="https://t.me/Irina_Krechet")],
        [InlineKeyboardButton(text="📢 Анонси", url="https://t.me/krechetirina")],
 	[InlineKeyboardButton(text="📢 Мій Канал", url="https://t.me/kgxtni")],
        [InlineKeyboardButton(text="🔮 Магічна Майстерня", url="https://t.me/krechetirina")]
    ])
    return keyboard

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привіт! Я Бот Ірини Кондратюк. Обери що саме тебе цікавить:", reply_markup=get_main_menu())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
