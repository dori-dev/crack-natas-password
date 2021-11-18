"""Cracking natas password!
"""

# Third party import
from requests import post

# Local imports
from required import auth, URL, CHARS
from required import send_request
password = ""



while len(password) <= 32:
    for test_char in CHARS:
        send_request()
