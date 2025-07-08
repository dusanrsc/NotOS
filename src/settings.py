# settings.py

# Imports Section.
# Importing Modules Section.
import data

# Importing Sub-Modules Section.
from datetime import date, datetime

# NotOS Global Settings Section.
# CONSTANTS Section.
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 850

METADATA = f"{data.PROJECT_NAME} {data.__version__} by: {data.__developer_tag__}"

SCREEN_ABSTRACTION_BORDER_RADIUS = 10

DEFAULT_NAVBAR_HEIGHT = 40
DEFAULT_NAVBAR_BUTTON_FONT_SIZE = 30

SYSTEM_KEYBOARD_ELEMENT_PADDING = 2

# Global Variable Section.
navigation_id = 0

day_today = date.today()
time_now = datetime.now().time().strftime(" %H:%M ")

battery_level = 100

# List Section.
navigation_list = ["home", "phone", "camera", "sms"]
screen_mode_options = ["dark", "light"]

screen_mode = screen_mode_options[0]
screen_mode_color_handler = None

system_keyboard_key_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "SHIFT" , "Z", "X", "C", "V", "B", "N", "M", "BACKSPACE", "SYMBOLS", ",", "SPACEBAR", ".", "NEXT"]
system_keyboard_key_down_list = []
