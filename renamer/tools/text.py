from pyrogram.emoji import *

class TEXT:
    DOWNLOAD_START = f"iam downloading your file just wait βΊοΈ{SLEEPING_FACE}"
    UPLOAD_START = f"iam trying to upload your file βΊοΈ{SLEEPING_FACE}"
    UPLOAD_SUCESS = f"Thanks for using [my dev](https://t.me/basildmx)"
    BANNED_USER_TEXT = f"Hey bro, you are **banned** from using me {FACE_WITH_TEARS_OF_JOY}."
    NOT_LOGGED_TEXT = f"This bot was only for private use {LOCKED_WITH_KEY}. If you want to use this bot you need to send me correct password in the format `/login bot_password`"
    SAVED_CUSTOM_THUMBNAIL = f"Thumbnail Saved Permanently {NOTEBOOK_WITH_DECORATIVE_COVER}"
    DELETED_CUSTOM_THUMBNAIL = f"Thumbnail Deleted Successfully {CHECK_MARK_BUTTON}"
    NO_CUSTOM_THUMB_NAIL_FOUND = f"π­π πππππ»ππΊππ π₯ππππ½ {THUMBS_DOWN_LIGHT_SKIN_TONE}"
    THUMBNAIL_CAPTION = f"{BACKHAND_INDEX_POINTING_UP_LIGHT_SKIN_TONE} Your Permanent thumbnail"


    ABOUT = """**π¬π π£πΎππΊπππ :**

** My Name:** {bot_name}
    
** Language:** [Python 3](https://www.python.org/)

** FrameWork:** [Pyrogram](https://github.com/pyrogram/pyrogram)

** Developer:** {bot_owner}

** Channel:** [here](https://t.me/dmx_all)

** Group:** [here](https://t.me/dmx_chating)


"""

    HELP_USER = """**Follow Below Steps:**
   
βοΈοΈοΈ Use /mode command to change upload mode.
βοΈοΈοΈ Send a photo to set as permanent thumbnail.
βοΈοΈοΈ Now send me the Telegram file you want to rename.
βοΈοΈοΈ Send the new name when bot ask.

For source code check about
"""

    START_TEXT = """Hi {user_mention},

I am a telegram renamer with permanent thumbnail. ONLY FOR DMX GROUP

π₯ππ π¬πππΎ π£πΎππΊπππ π²πΎπΎ π§πΎππ.

**Maintained By:** {bot_owner}
"""
