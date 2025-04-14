from time import time
from .botsetup import Bot, CONFIG, load_handlers, logger
from bot.helper.button_maker import ButtonMaker

# constants
__version__ = "0.1.0.3 (beta)" # major.minor.patch.commits
BOT_UPTIME = time()

# Main bot function
bot = Bot(CONFIG.BOT_TOKEN)

load_handlers() #needs to be after Bot instantiation

logger.info(f"""
Developed by
 ______     __     ______     __  __     ______     __        
/\  == \   /\ \   /\  ___\   /\ \_\ \   /\  __ \   /\ \       
\ \  __<   \ \ \  \ \___  \  \ \  __ \  \ \  __ \  \ \ \____  
 \ \_____\  \ \_\  \/\_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_/   \/_____/   \/_/\/_/   \/_/\/_/   \/_____/ 
   
    Version: {__version__}
    Library: python-telegram-bot
    Init Release: Jan 2 2023
    Rebuilt: April 14 2025
    GitHub: https://github.com/bishalqx980
""")
