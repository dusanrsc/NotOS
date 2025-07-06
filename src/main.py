# Imports Section.
# Importing Sub-Modules Section.
from flet import *
import data

# Program Settings Section.
# CONSTANTS Section.
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 850

METADATA = f"{data.PROJECT_NAME} {data.__version__} by: {data.__developer_tag__}"

# Hexadecimal Color CONSTANTS Section.
# Basic Hexadecimal Color CONSTANTS Section.
RED   = "#FF0000"
GREEN = "#00FF00"
BLUE  = "#0000FF"

BLACK = "#000000"
GRAY  = "#333333"
WHITE = "#FFFFFF"

ALPHA = GREEN

# Custom Hexadecimal Color CONSTANTS Section.
DARK_GREEN = "#005500"

# Default Hexadecimal CONSTANTS Colors Section.
DEFAULT_DARK_MODE  = BLACK
DEFAULT_LIGHT_MODE = WHITE

DEFAULT_PAGE_COLOR = GRAY
DEFAULT_SCREEN_AB_COLOR = DEFAULT_DARK_MODE

# Main Program Logic Section.
def main(page: Page):

    # Main Page Window Settings Section
    page.title = METADATA
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.resizable = False       # Conditionaly
    page.bgcolor = DEFAULT_PAGE_COLOR
    page.update()

    # Creating Container Widget.
    screen_abstraction = Container(
        border_radius=35,
        expand=True,
        bgcolor=DEFAULT_SCREEN_AB_COLOR,
        alignment=alignment.bottom_center,
        
        content=Container(height=50, expand=True, bgcolor=DARK_GREEN))
    
    # Rendering Parent Container Widget Into A Page. 
    page.add(screen_abstraction)
    
# Rendering The Main Window - Starting The Program!
app(target=main)
