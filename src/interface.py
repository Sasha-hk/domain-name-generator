import os

from termcolor2 import c

from .generate_domain import generate_domain
from .file_write import FileWrite


class UI:
    """Console interface to generate domain"""

    def __init__(self):
        self.domains = []
        self.current_domain = ''
        self.location = ''
        self.min_length = 0
        self.max_length = 0
        self.file_write = FileWrite()

    def start(self):
        self.clear_console()
        self.get_help()
        self.get_location()
        self.get_domain_length()
        self.make_domain()

        while True:
            self.clear_console()
            self.menu_controller()

            key = input()

            self.handle_key(key)

    def handle_key(self, key):
        """Handel press key"""
        if key == 'x':
            self.exit()

        elif key == 'a':
            self.add_domain()

        elif key == 's' or key == 'n':
            self.scip_domain()

        elif key == 'h':
            self.get_help()

    def make_domain(self):
        self.current_domain = generate_domain(
            self.min_length,
            self.max_length,
            self.location
        )

    def menu_controller(self):
        """Controller menu"""
        self.clear_console()
        self.print_menu()

    def clear_console(self):
        """Clear console"""
        command = 'clear'

        if os.name in ('nt', 'dos'):
            command = 'cls'

        os.system(command)

    def print_menu(self):
        if self.domains:
            print('Selected domains: ')
            for domain in self.domains:
                print(f'  {domain}')

        print('\nGenerated domain: ', self.current_domain)

        self.get_input_view()

    def add_domain(self):
        self.file_write.update_to_selected(self.current_domain)
        self.domains.append(self.current_domain)
        self.make_domain()

    def scip_domain(self):
        self.file_write.update_to_all(self.current_domain)
        self.current_domain = ''
        self.make_domain()

    def get_location(self):
        print('\nEnter location, for example .com ')

        self.location = self.not_blank_input()

    def get_domain_length(self):
        print('\nEnter minimum domain length')
        self.min_length = int(self.not_blank_input())

        print('\nEnter maximum doman length')
        self.max_length = int(self.not_blank_input())

    def not_blank_input(self):
        input_value = ''

        while input_value == '':
            input_value = self.get_input()

        return input_value

    def get_input(self) -> str:
        x = input(c(' > ').green)

        return x

    def get_input_view(self):
        print(c(' > ').green, end='')

    def get_help(self):
        """Short info about function"""
        self.clear_console()
        print(
            'Enter:',
            '\n   x     - to exit',
            '\n   h     - get help',
            '\n   s / n - skip domain',
            '\n   a     - add domain'
        )

        input(c('\nPress Enter to start! ').green)

    def exit(self):
        self.clear_console()
        exit(0)
