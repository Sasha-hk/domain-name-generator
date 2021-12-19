from pathlib import Path
import os

from dotenv import load_dotenv
from termcolor2 import c
import keyboard


BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / '.env')
