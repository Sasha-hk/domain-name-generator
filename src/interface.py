import os

from pynput import keyboard
from termcolor2 import c

from . import check_domain
from . import generate_domain


class UI:
    """Console interface to generate domain"""
    is_press = False

    def __init__(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            self.menu_controller()
            listener.join()

    def on_press(self, key):
        """Handel press key"""
        if not self.is_press:
            self.is_press = True
            try:
                if key.char == 'x':
                    exit(0)

                else:
                    self.menu_controller()

            except AttributeError:
                if key.name == 'enter':
                    self.menu_controller()

                elif key.name == 'space':
                    self.menu_controller()

                elif key.name == 'esc':
                    exit(0)
                else:
                    self.menu_controller()

    def on_release(self, key):
        self.is_press = False

    def menu_controller(self):
        """Controller menu"""
        self.clear_console()
        self.print_menu()

    def clear_console(self):
        """Clear console"""
        os.system('clear')

    def print_menu(self):
        """Print menu"""
        print(
            'Enter',
            '\n   x     - to exit',
            '\n   space - skip doman',
            '\n   enter - add domain'
        )
        print(c(' > ').green, end='')

    def add_domain(self):
        pass

    def scip_domain(self):
        pass
