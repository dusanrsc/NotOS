# Imports Section.
# Importing Modules Section.
import metadata

# Importing Sub-Modules Section.
from flet import *
from settings import *
from colors import *

# Main NotOS Logic Section.
def main(page: Page):

    # Local Logic For Screen Mode!
    if screen_mode == screen_mode_options[0]:
        screen_mode_color_handler = BLACK
    else:
        screen_mode_color_handler = WHITE

    # NotOS Local Settings Section.
    # WINDOW_WIDTH  = page.window.width
    # WINDOW_HEIGHT = page.window.height

    # Local Functions Section.
    # Get Screen Size Function.
    def get_screen_size(data_type="float") -> float | int | str:

        # Default/Float Data Type Condition.
        if data_type == "float":
            screen_width = float(page.window.width)
            screen_height = float(page.window.height)

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
            screen_width = float(page.window.width)
            screen_height = float(page.window.height)

            print("Error: Wrong Data Type! Choice Between: 'float: Default', 'int: Integer' and 'str: String'!")

        return screen_width, screen_height

    # Go Back Navigation Function.
    def go_back_navigation(event) -> str:

        # Global Variable.
        global navigation_id

        # Navigation Logic Section.
        if navigation_id > 0:
            navigation_id -= 1

        # Return Current Navigation
        return navigation_list[navigation_id]

    # Bootstrap Console Function.
    def bootstrap_console() -> None:

        # { Write Your Code Here! }
        pass # Placeholder!

    # Setting Up Screen Mode(Dark/Light).
    def set_screen_mode() -> None:

        # Switching Condition.
        if screen_abstraction.bgcolor == BLACK:
            screen_abstraction.bgcolor = WHITE
        else:
            screen_abstraction.bgcolor = BLACK

        # Updating Screen Abstraction.
        screen_abstraction.update()

    # Show System Keyboard From Function{Button Press}.
    def render_system_keyboard() -> None:

        # Global Variable.
        global show_system_keyboard

        # Switching Condition.
        if show_system_keyboard:
            show_system_keyboard = False
        else:
            show_system_keyboard = True

    # System Keyboard Key Down.
    def system_keyboard_key_down(event, key=None) -> None:

        # Global Variable.
        global system_keyboard_key_down_list

        # Adding Key In The List.
        system_keyboard_key_down_list.append(key)

    # Only In Development Stage!
    # Printing Development Stage Data Function.
    def print_development_data() -> None:
        
        # Only In Development Stage!
        # Printing Parameters While Developing The App.
        print(get_screen_size(data_type="float"))
        print(navigation_list)
        print(navigation_list[navigation_id])
        print(set_screen_mode())
        print(f"show_system_keyboard: {show_system_keyboard}")
        print(f"system_keyboard_key_down_list: {system_keyboard_key_down_list}")

    # Main Page Window Settings Section
    page.title = METADATA
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.window.resizable = False # Conditionaly
    page.bgcolor = DEFAULT_PAGE_COLOR
    page.update()

    # Content Widgets Section.
    today_text_widget = Text(day_today)
    now_text_widget = Text(time_now, color=BLACK)

    battery_text_widget = Text(f"{battery_level}%🔋", color=BLACK)

    system_keyboard = Container(
        bgcolor=DARK_GRAY,
        padding=SYSTEM_KEYBOARD_ELEMENT_PADDING,
        alignment=alignment.bottom_center,
        content=Column(
            spacing=SYSTEM_KEYBOARD_ELEMENT_PADDING,
            controls=[
                Container(height=get_screen_size(data_type="int")[0] // 400),
                Row(
                    controls=[
                        ElevatedButton(text="1", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "1")), 
                        ElevatedButton(text="2", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "2")), 
                        ElevatedButton(text="3", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "3")), 
                        ElevatedButton(text="4", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "4")), 
                        ElevatedButton(text="5", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "5")), 
                        ElevatedButton(text="6", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "6")), 
                        ElevatedButton(text="7", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "7")), 
                        ElevatedButton(text="8", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "8")), 
                        ElevatedButton(text="9", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "9")), 
                        ElevatedButton(text="0", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "0"))],
                        spacing=SYSTEM_KEYBOARD_ELEMENT_PADDING
                    ),

                Row(
                    controls=[
                        ElevatedButton(text="Q", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "Q")), 
                        ElevatedButton(text="W", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "W")), 
                        ElevatedButton(text="E", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "E")), 
                        ElevatedButton(text="R", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "R")), 
                        ElevatedButton(text="T", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "T")), 
                        ElevatedButton(text="Y", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "Y")), 
                        ElevatedButton(text="U", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "U")), 
                        ElevatedButton(text="I", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "I")), 
                        ElevatedButton(text="O", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "O")), 
                        ElevatedButton(text="P", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "P"))],
                        spacing=SYSTEM_KEYBOARD_ELEMENT_PADDING
                    ),

                Row(
                    controls=[
                        Container(expand=True),
                        ElevatedButton(text="A", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "A")), 
                        ElevatedButton(text="S", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "S")), 
                        ElevatedButton(text="D", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "D")), 
                        ElevatedButton(text="F", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "F")), 
                        ElevatedButton(text="G", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "G")), 
                        ElevatedButton(text="H", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "H")), 
                        ElevatedButton(text="J", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "J")), 
                        ElevatedButton(text="K", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "K")), 
                        ElevatedButton(text="L", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "L")),
                        Container(expand=True)],
                        spacing=SYSTEM_KEYBOARD_ELEMENT_PADDING
                    ),

                Row(
                    controls=[
                        # △⯅
                        ElevatedButton(text="⯅", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "SHIFT")),  
                        ElevatedButton(text="Z", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "Z")), 
                        ElevatedButton(text="X", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "X")), 
                        ElevatedButton(text="C", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "C")), 
                        ElevatedButton(text="V", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "V")), 
                        ElevatedButton(text="B", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "B")), 
                        ElevatedButton(text="N", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "N")), 
                        ElevatedButton(text="M", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "M")), 
                        ElevatedButton(text="⌫", expand=True, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "BACKSPACE"))],
                        spacing=SYSTEM_KEYBOARD_ELEMENT_PADDING
                    ),

                Row(
                    controls=[
                        ElevatedButton(text="!#1",   expand=True,  style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "SYMBOLS")), 
                        ElevatedButton(text=",",     expand=False, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, ",")), 
                        ElevatedButton(text="English", expand=True,  style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "SPACEBAR")), 
                        ElevatedButton(text=".",     expand=False, style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, ".")), 
                        ElevatedButton(text="NEXT",  expand=True,  style=ButtonStyle(shape=RoundedRectangleBorder(radius=5)), on_click=lambda event: system_keyboard_key_down(None, "NEXT"))],
                        spacing=SYSTEM_KEYBOARD_ELEMENT_PADDING
                    ),
                        Container(height=get_screen_size(data_type="int")[0] // 400),
                ],
            ),
        )

    # Creating And Rendering Screen Abstraction Widget.
    # With Showed System Keyboard Condition.
    if show_system_keyboard:
        screen_abstraction = Container(
            border_radius=SCREEN_ABSTRACTION_BORDER_RADIUS,
            expand=True,
            bgcolor=screen_mode_color_handler,
            alignment=alignment.bottom_center,
            
            content=Column(spacing=0, expand=True, controls=[

                    # Rendering Status Bar.
                    Container(
                        height=(DEFAULT_NAVBAR_HEIGHT // 1.75),
                        bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                        alignment=alignment.center_left,
                        content=Row([now_text_widget, Container(expand=True), battery_text_widget])
                    ),

                    # Rendering Abstraction Of The Main Screen.
                    Container(expand=True),

                    # Rendering System Keyboard.
                    system_keyboard,

                    # Rendering Navigation Bar.
                    Container(
                        height=DEFAULT_NAVBAR_HEIGHT,
                        bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                        content=Row(
                            controls=[

                                # Rendering Navigation Bar Buttons.
                                ElevatedButton(
                                    text="lll",
                                    elevation=False,
                                    expand=True,
                                    color=DEFAULT_NAVBAR_COLOR,
                                    bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                                    style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)),
                                    on_click=lambda event: None,
                                ),
                                ElevatedButton(
                                    text=" ▢ ",
                                    elevation=False,
                                    expand=True,
                                    color=DEFAULT_NAVBAR_COLOR,
                                    bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                                    style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)),
                                    on_click=lambda event: None,
                                ),
                                ElevatedButton(
                                    text=" ⤶ ",
                                    elevation=False,
                                    expand=True,
                                    color=DEFAULT_NAVBAR_COLOR,
                                    bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                                    style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)),
                                    on_click=lambda event: print_development_data(),
                                ),
                            ],
                            spacing=(get_screen_size(data_type="int")[0] // 10),
                        ),
                    ),
                ],
            ),
        )

    # Without Showed System Keyboard Condition.
    else:
        screen_abstraction = Container(
            border_radius=SCREEN_ABSTRACTION_BORDER_RADIUS,
            expand=True,
            bgcolor=screen_mode_color_handler,
            alignment=alignment.bottom_center,
            
            content=Column(spacing=0, expand=True, controls=[

                    # Rendering Status Bar.
                    Container(
                        height=(DEFAULT_NAVBAR_HEIGHT // 1.75),
                        bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                        alignment=alignment.center_left,
                        content=Row([now_text_widget, Container(expand=True), battery_text_widget])
                    ),

                    # Rendering Abstraction Of The Main Screen.
                    Container(expand=True),

                    # Rendering Navigation Bar.
                    Container(
                        height=DEFAULT_NAVBAR_HEIGHT,
                        bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                        content=Row(
                            controls=[

                                # Rendering Navigation Bar Buttons.
                                ElevatedButton(
                                    text="lll",
                                    elevation=False,
                                    expand=True,
                                    color=DEFAULT_NAVBAR_COLOR,
                                    bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                                    style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)),
                                    on_click=lambda event: None,
                                ),
                                ElevatedButton(
                                    text=" ▢ ",
                                    elevation=False,
                                    expand=True,
                                    color=DEFAULT_NAVBAR_COLOR,
                                    bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                                    style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)),
                                    on_click=lambda event: render_system_keyboard(),
                                ),
                                ElevatedButton(
                                    text=" ⤶ ",
                                    elevation=False,
                                    expand=True,
                                    color=DEFAULT_NAVBAR_COLOR,
                                    bgcolor=DEFAULT_NAVBAR_BACKGROUND_COLOR,
                                    style=ButtonStyle(text_style=TextStyle(size=DEFAULT_NAVBAR_BUTTON_FONT_SIZE)),
                                    on_click=lambda event: print_development_data(),
                                ),
                            ],
                            spacing=(get_screen_size(data_type="int")[0] // 10),
                        ),
                    ),
                ],
            ),
        )

    # Rendering Parent Container Widget Into A Page. 
    page.add(screen_abstraction)
    
# Rendering The Main Window - Starting The NotOS!
app(target=main)