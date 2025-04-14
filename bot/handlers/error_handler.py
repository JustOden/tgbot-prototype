from telegram import Update
from telegram.ext import ContextTypes
from config import logger, bot


@bot.error_handler()
async def default_error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(context.error)