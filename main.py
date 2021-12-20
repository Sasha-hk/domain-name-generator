import os
from pathlib import Path

from dotenv import load_dotenv
from termcolor2 import c

from src.interface import UI


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / '.env')


def main():
    ui = UI()

    ui.start()


if __name__ == '__main__':
    main()
