async def process_start(message):
    await message.answer(text=f"Here is the script: https://github.com/marbleyung/TG_Scrap")


def register_user_handlers(dp):
    dp.register_message_handler(process_start, commands=['start'])
