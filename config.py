#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "<b>Heya {first} 👋 I'm @Adaarfilter_bot !\n\n⚠️📌 ᴡᴇ ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ᴀʟʟ ᴛᴏʀᴇɴᴛ ꜰɪʟᴇꜱ ꜰɪʀꜱᴛ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ, torrentൽ വരുന്ന എല്ലാ ഫയലും ആദ്യം തന്നെ ഞ്ങ്ങൾ upload ചെയ്യുന്നതാണ്, हम हर टोरेंट फाइल को पहले अपलोड करते हैं\n\n⚠️📌 ᴡᴇ ᴡᴏɴ'ᴛ ᴘʀᴏᴠɪᴅᴇ ʏᴇꜱꜱᴍᴀᴀ ꜱᴇʀɪᴇꜱ ᴀɴᴅ ᴛʜɪꜱ ʙᴏᴛ ᴡᴏɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ ᴘᴏʀɴᴏɢʀᴀᴘʜɪᴄ ᴄᴏɴᴛᴇɴᴛꜱ, ഞങ്ങൾ yessma സീരീസും അശ്ലീല വീഡിയോകളും promote ചെയ്യുന്നത് അല്ല, हम येस्मा सीरीज प्रदान नहीं करेंगे और यह बॉट अश्लील सामग्री को बढ़ावा नहीं दे सकता है\n\n https://t.me/+vg2zU33d_1c2YmQ1 👈 Mᴏᴠɪᴇ RᴇQᴜᴇꜱᴛ Hᴇʀᴇ , മൂവി ഇവിടെ ചോദിക്കുക, यहां फिल्म के लिए पूछें..!!!\n\n<u>Powered by ഉർവശി തീയറ്റേഴ്‌സ്™</u></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>Hello {first}</b>\n\n<u><b>♦️ READ THIS INSTRUCTION ♦️</b></u>\n\n <i>🗣 നിങ്ങൾ ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള ചാനലിൽ ജോയിൻ ചെയ്യണം. ജോയിൻ ചെയ്ത ശേഷം വീണ്ടും ഗ്രൂപ്പിൽ പോയി ആ ബട്ടനിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ പ്രൈവറ്റ് ആയി അയച്ചു തരുന്നതാണ്..😍\n\n</i>  <i>🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈\n\n</i>  <u><b>👇JOIN THIS CHANNEL & TRY</b>👇</u>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
