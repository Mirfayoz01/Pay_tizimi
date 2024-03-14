import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from root import TOKEN
from bottons import menu, catMenu, inlineBtn
from Payments import order_1, pre_checkout_query, successful_payment, pre_checkout_query2, order_2, order_3, pre_checkout_query3, pre_checkout_query4, order_4

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello", reply_markup=menu)


@dp.message(F.text == "Category")
async def category(message: Message):
    await message.answer("Choose", reply_markup=catMenu)


@dp.message(F.text == "Product 1")
async def product_1(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                               caption="Iphone 15 Pro Max\n"
                                       "Battery Level: 100%\n", reply_markup=inlineBtn)

@dp.message(F.text == "Products 2") # noqa
async def product_1(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                               caption="Iphone 14 Pro Max\n"
                                       "Battery Level: 100%\n", reply_markup=inlineBtn)

@dp.message(F.text == "Product 3") # noqa
async def product_1(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                               caption="Iphone 13 Pro Max\n"
                                       "Battery Level: 100%\n", reply_markup=inlineBtn)


@dp.message(F.text == "Products 4") # noqa
async def product_1(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                               caption="Iphone 12 Pro Max\n"
                                       "Battery Level: 100%\n", reply_markup=inlineBtn)



dp.callback_query.register(order_1, F.data == "pay_1") # noqa
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_2, F.data == "pay_1") # noqa
dp.pre_checkout_query.register(pre_checkout_query2)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_3, F.data == "pay_1") # noqa
dp.pre_checkout_query.register(pre_checkout_query3)
dp.message.register(successful_payment, F.successful_payment)

dp.callback_query.register(order_4, F.data == "pay_1") # noqa
dp.pre_checkout_query.register(pre_checkout_query4)
dp.message.register(successful_payment, F.successful_payment)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main()) # noqa