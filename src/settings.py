# settings.py

# Imports Section.
# Importing Modules Section.
import metadata

# Importing Sub-Modules Section.
from datetime import date, datetime

# NotOS Global Settings Section.
# CONSTANTS Section.
WINDOW_WIDTH: int  = 400
WINDOW_HEIGHT: int = 850

PROJECT_NAME: str = "NotOS"

METADATA: str = f"{PROJECT_NAME} {metadata.__version__} github: {metadata.__developer__}"

SCREEN_ABSTRACTION_BORDER_RADIUS: int = 10

DEFAULT_NAVBAR_HEIGHT: int = 40
DEFAULT_NAVBAR_BUTTON_FONT_SIZE: int = 30

SYSTEM_KEYBOARD_ELEMENT_PADDING: int = 4

# Global Variable Section.
navigation_id: int = 0

day_today: int = date.today()
time_now: str = datetime.now().time().strftime(" %H:%M ")

battery_level: int = 100

# List Section.
navigation_list: list = ["home", "phone", "camera", "sms"]
screen_mode_options: list = ["dark", "light"]

screen_mode: str = screen_mode_options[0]
screen_mode_color_handler: bool = None

system_keyboard_key_list: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "SHIFT" , "Z", "X", "C", "V", "B", "N", "M", "BACKSPACE", "SYMBOLS", ",", "SPACEBAR", ".", "NEXT"]
system_keyboard_key_down_list: list = []

show_system_keyboard: bool = True