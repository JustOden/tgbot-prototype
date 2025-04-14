import asyncio
from telegram import BotCommand, BotCommandScope
from telegram.constants import ParseMode
from config import bot, CONFIG, logger


@bot.post_init
async def post_init(app):
    bot_commands = [
    BotCommand("start", "Introducing...")
    ]
    
    try:
        # bot commands only for PRIVATE chats
        await app.set_my_commands(bot_commands, BotCommandScope(BotCommandScope.ALL_PRIVATE_CHATS))
    except Exception as e: 
        logger.error(e) 
    
    await app.bot.send_message(CONFIG.OWNER_ID, "<b>Bot Started!</b>", parse_mode=ParseMode.HTML)


def main():
    bot.run()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(main())
    loop.run_forever()
