from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from keyboards import *
from texno_pars import pars_texno
from aiogram.types import Message
from configs import get_value

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer('Hush kelibsiz Texnomartga )')
    await show_category_texno(message)


async def show_category_texno(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Kategoriyani tanlang!',
                           reply_markup=buttons_category())


@dp.message_handler(content_types=['text'])
async def get_texno_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_news = pars_texno(get_value(category_text))

    for product in get_news:
        images = product.get('images')
        credit_price = product.get('credit_price')
        price = product.get('price')
        content = product.get('content')

        await message.answer_photo(photo=images, parse_mode='html', caption=f'''
<b>Oyma oy:</b> {credit_price}
<b>Naqd:</b> {price}''', reply_markup=button_link(content))




executor.start_polling(dp)
