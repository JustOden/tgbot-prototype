from telegram import Update
from telegram.ext import ContextTypes
from bot import __version__
from ..helper.button_maker import ButtonMaker

async def handle_callbackquery(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    query = update.callback_query

    # refined query data
    query_data = query.data.removeprefix("menu_")

    if query_data == "none":
        await query.answer()
        return
    
    elif query_data == "help":
        text = "Currently I can do nothing 💀. Im underdevelopment."
        btn_data = [{"BACK": "menu_back"}]
    
    elif query_data == "about":
        text = (
            "<blockquote>About Me</blockquote>\n\n"

            f"Name: {context.bot.first_name}\n"
            f"ID: <code>{context.bot.id}</code>\n"
            f"Username: {context.bot.name}\n\n"

            "Developed with Python 3.11\n"
            "Library: PTB\n"
            "Initial release: Jan 2, 2023\n"
            "Rebuilt: April 14, 2025"
        )

        btn_data = [{"BACK": "menu_back"}]
    
    elif query_data == "back":
        text = (
            f"Hi, {user.first_name}. I'm {context.bot.first_name}.\n\n"
            f"<b>Version: </b> <code>{__version__}</code>"
        )

        btn_data = [
            {"HELP": "menu_help", "About": "menu_about"},
            {"Source": "https://github.com/bishalqx980/tgbot-prototype", "Dev": "https://t.me/bishalqx680/22"}
        ]
    
    # global edit
    btn = ButtonMaker.cbutton(btn_data)
    await query.edit_message_text(text, reply_markup=btn)
