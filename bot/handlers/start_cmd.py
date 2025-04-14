from telegram import Update
from telegram.ext import ContextTypes
from config import __version__, bot, ButtonMaker


@bot.command_handler("start")
async def func_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    effective_message = update.effective_message

    text = (
        f"Hi, {user.first_name}. I'm {context.bot.first_name}.\n\n"
        f"<b>Version: </b> <code>{__version__}</code>"
    )

    btn_data = [
        {"HELP": "menu_help", "About": "menu_about"},
        {"Source": "https://github.com/bishalqx980/tgbot-prototype", "Dev": "https://t.me/bishalqx680/22"}
    ]

    btn = ButtonMaker.cbutton(btn_data)
    await effective_message.reply_text(text, reply_markup=btn)
