# Imports Section.
# Importing Modules Section.
import data

# Importing Sub-Modules Section.
from flet import *

# NotOS Global Settings Section.
# CONSTANTS Section.
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 850

METADATA = f"{data.PROJECT_NAME} {data.__version__} by: {data.__developer_tag__}"

SCREEN_ABSTRACTION_BORDER_RADIUS = 20

# Hexadecimal Color CONSTANTS Section.
# Basic Hexadecimal Color CONSTANTS Section.
RED   = "#FF0000"
GREEN = "#00FF00"
BLUE  = "#0000FF"

BLACK = "#000000"
WHITE = "#FFFFFF"

ALPHA = GREEN

# Custom Hexadecimal Color CONSTANTS Section.
GRAY  = "#333333"
DARK_GRAY = "#111111"
DARK_GREEN = "#005500"

# Default Hexadecimal CONSTANTS Colors Section.
DEFAULT_DARK_MODE  = BLACK
DEFAULT_LIGHT_MODE = WHITE

DEFAULT_PAGE_COLOR = GRAY
DEFAULT_SCREEN_ABSTRACTION_COLOR = DEFAULT_DARK_MODE

DEFAULT_NAVBAR_COLOR = BLACK
DEFAULT_NAVBAR_BACKGROUND_COLOR = WHITE

DEFAULT_NAVBAR_BUTTON_FONT_SIZE = 30

# Main NotOS Logic Section.
def main(page: Page):

    # NotOS Local Settings Section.
    # WINDOW_WIDTH  = page.window.width
    # WINDOW_HEIGHT = page.window.height

    # Local Functions Section.
    # Get Screen Size Function.
    def get_screen_size(data_type="float") -> float | int | str:

        # Default/Float Data Type Condition.
        if data_type == "float":
            screen_width = page.window.width
            screen_height = page.window.height

        # Integer Data Type Condition.
        elif data_type == "int":
            screen_width = int(page.window.width)
            screen_height = int(page.window.height)

        # String Data Type Condition.
        elif data_type == "str":
            screen_width = str(page.window.width)
            screen_height = str(page.window.height)

            # Error Handler Condition!
            # Explicitly Setting Up Data Type As Float Due To Potential Changes At The 'Flet' Framework Level Itself.
        else:
            print("Error: Wrong Data Type! Choice Between: 'float: Default', 'int: Integer' and 'str: String'!")

            screen_width = float(page.window.width)
            screen_height = float(page.window.height)

        return screen_width, screen_height

    # Only In Development Stage!
    print(get_screen_size(data_type="None"))

    # Bootstrap Console Function.
    def bootstrap_console() -> None:

        # { Write Your Code Here! }
        pass # Placeholder!

    # Setting Up Screen Mode(Dark/Light).
    def set_screen_mode() -> None:

        # { Write Your Code Here! }
        pass # Placeholder!

    # Main Page Window Settings Section
    page.title = METADATA
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.resizable = False       # Conditionaly
    page.bgcolor = DEFAULT_PAGE_COLOR
    page.update()

    # Content Widgets Section.
    # { Write Your Code Here! }

    # Creating Container Widget.
    screen_abstraction = Container(
        border_radius=SCREEN_ABSTRACTION_BORDER_RADIUS,
        expand=True,
        bgcolor=DEFAULT_SCREEN_ABSTRACTION_COLOR,
        alignment=alignment.bottom_center,
        
        # Navigation Bar Section!
        # (get_screen_size(data_type="int")[1] // 20)
        content=Container(height=40, expand=True, bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR, content=Row(
            controls=[
                ElevatedButton(text="  lll  ", elevation=False, expand=True, color=DEFAULT_NAVBAR_COLOR, bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR, style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)), on_click=lambda event: None),
                ElevatedButton(text="   O   ", elevation=False, expand=True, color=DEFAULT_NAVBAR_COLOR, bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR, style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)), on_click=lambda event: None),
                ElevatedButton(text="   V   ", elevation=False, expand=True, color=DEFAULT_NAVBAR_COLOR, bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR, style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)), on_click=lambda event: None),
            ],
            # Set Dynamic Spacing By Screen Width Divided By N.
            spacing=(get_screen_size(data_type="int")[0] // 10)
            )
        )
    )
    
    # Rendering Parent Container Widget Into A Page. 
    page.add(screen_abstraction)
    
# Rendering The Main Window - Starting The NotOS!
app(target=main)
