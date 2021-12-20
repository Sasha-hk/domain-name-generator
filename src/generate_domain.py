from random import choice
from string import ascii_lowercase


def generate_domain(min: int, max: int, location: str) -> str:
    length = choice(range(min, max))
    domain_result = ''

    i = 0
    while i < length:
        domain_result += choice(ascii_lowercase)
        i += 1

    return domain_result + location
