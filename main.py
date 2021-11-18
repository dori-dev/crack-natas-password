"""Cracking natas password!
"""

# Third party import
from requests import post

# Local imports
from required import auth, URL, CHARS


password = ""


def send_request():
    pass


while len(password) <= 32:
    for test_char in CHARS:
        send_request()
