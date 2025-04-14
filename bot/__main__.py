import asyncio
from telegram import Update, LinkPreviewOptions, BotCommand, BotCommandScope
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    Defaults
)

from telegram.constants import ParseMode
from config import CONFIG
from bot import bot, logger
from bot.func.start_cmd import func_start
from bot.func.query_handler import handle_callbackquery

async def post_init():
    # bot commands
    bot_commands = [
        BotCommand("start", "Introducing...")
    ]
    
    try:
        # bot commands only for PRIVATE chats
        await bot.set_my_commands(bot_commands, BotCommandScope(BotCommandScope.ALL_PRIVATE_CHATS))
    except Exception as e:
        logger.error(e)
    
    await bot.send_message(CONFIG.OWNER_ID, "<b>Bot Started!</b>", parse_mode=ParseMode.HTML)


async def default_error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(context.error)


def main():
    default_param = Defaults(
        parse_mode=ParseMode.HTML,
        link_preview_options=LinkPreviewOptions(is_disabled=True),
        block=False,
        allow_sending_without_reply=True
    )
    # Bot instance
    application = ApplicationBuilder().token(CONFIG.BOT_TOKEN).defaults(default_param).build()

    # Main handlers
    application.add_handler(CommandHandler("start", func_start))

    # Callback query handlers
    application.add_handler(CallbackQueryHandler(handle_callbackquery))
    # Error handler
    application.add_error_handler(default_error_handler)
    # Check Updates
    application.run_polling(allowed_updates=Update.ALL_TYPES)


async def app_init():
    # other post init func will be placed here
    await post_init()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(app_init())
    loop.create_task(main())
    loop.run_forever()
