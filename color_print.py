import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, *effects: str) -> None:
    """
    Print 'text' using the ANSI sequences to change color, etc.

    :param text:    The text to print.
    :param effects:  The effect we want. One of the constants
        defined at the start of this module.
    """
    effect_sting = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_sting, text, RESET)
    print(output_string)

colorama.init()
color_print("Hello, Red", RED)
color_print("Hello, Red in BOLD", RED, BOLD)
# test that the colour was reset
print("This should be in the default terminal colour")
color_print("Hello, Blue", BLUE)
color_print("Hello, Blue reversed", BLUE, REVERSE)
color_print("Hello, Blue reversed and underlined", BLUE, REVERSE, UNDERLINE)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, Yellow in BOLD", YELLOW, BOLD)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)
colorama.deinit()