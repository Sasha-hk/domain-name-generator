import os

from pynput import keyboard
from termcolor2 import c

# import check_domain
# import generate_domain


class UI:
    is_press = False

    def __init__(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            self.clear_console()
            listener.join()

    def on_press(self, key):
        if not self.is_press:
            self.is_press = True
            try:
                if key.char == 'x':
                    exit(0)

                else:
                    self.clear_console()

            except AttributeError:
                print(key.name)
                if key.name == 'enter':
                    print('enter')

                elif key.name == 'space':
                    print('space')

                elif key.name == 'esc':
                    print('Exit')
                    exit(0)
                else:
                    self.clear_console()

    def menu_controller(self):
        pass

    def on_release(self, key):
        self.is_press = False

    def clear_console(self):
        os.system('clear')

    def printMenu(self):
        print(
            'Enter',
            '\n\tx - to exit',
            '\n\tspace - to skip doman',
            '\n\tenter - to add domain'
        )
