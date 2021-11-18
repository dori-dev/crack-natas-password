"""Cracking natas password!
"""

# Third party import
from requests import post

# Local imports
from required import auth, URL, CHARS


password = ""


def get_respones(character):
    respones = post(URL, data={}, auth=auth)
    if "This user exists" in respones.text:
        return character
    return None


while len(password) <= 32:
    for test_char in CHARS:
        get_respones(test_char)
