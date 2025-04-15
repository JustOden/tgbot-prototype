import os
import importlib
from typing import Callable
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import Update, LinkPreviewOptions, BotCommand, BotCommandScope
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    Defaults
)
from telegram.constants import ParseMode
from .logger import setup_logging

# logger
logger = setup_logging()


class CONFIG:
    BOT_TOKEN = "" # STR
    OWNER_ID = 123 # INT


class Bot:
    commands: list[tuple[str, BotCommand]] = []

    def __init__(self, token: str):
        default_param = Defaults(
        parse_mode=ParseMode.HTML,
        link_preview_options=LinkPreviewOptions(is_disabled=True),
        block=False,
        allow_sending_without_reply=True
        )
        self.app = ApplicationBuilder().token(token).defaults(default_param).post_init(self.post_init).build()
    
    @staticmethod
    async def post_init(app):
        grouped_commands: dict[str, list[BotCommand]] = {scope: [] for scope, _ in Bot.commands}

        for scope, command in Bot.commands:
            grouped_commands[scope].append(command)

        try:
            for key, val in grouped_commands.items():
                await app.bot.set_my_commands(val, BotCommandScope(key))
                
        except Exception as e:
            logger.error(e)
        
        await app.bot.send_message(CONFIG.OWNER_ID, "<b>Bot Started!</b>", parse_mode=ParseMode.HTML)

    def error_handler(self):
        def decorator(func: Callable):
            self.app.add_error_handler(func)
            return func
        return decorator

    def command_handler(self, command_name="", description="", scope=BotCommandScope.DEFAULT):
        def decorator(func: Callable):
            name = command_name or func.__name__
            handler = CommandHandler(name, func)
            self.app.add_handler(handler)
            self.commands.append((scope, BotCommand(name, description or func.__doc__ or "No description provided")))
            return func
        return decorator

    def query_handler(self, query_name=""):
        def decorator(func: Callable):
            name = query_name or func.__name__
            handler = CallbackQueryHandler(func, f"{name}_[A-Za-z0-9]+")
            self.app.add_handler(handler)
            return func
        return decorator

    def message_handler(self, msg_filter=filters.ALL):
        def decorator(func: Callable):
            handler = MessageHandler(msg_filter, func)
            self.app.add_handler(handler)
            return func
        return decorator

    def run(self):
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


def load_handlers():
    for filename in os.listdir("./bot/handlers"):
        if filename.endswith(".py") and not filename.startswith("__"):
            importlib.import_module(f"handlers.{filename[:-3]}")