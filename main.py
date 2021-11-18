"""Cracking natas password!
"""

# Standart library imports
import requests
from string import ascii_letters, digits

characters = ascii_letters + digits
password = ""
url = "http://natas15.natas.labs.overthewire.org/index.php"
basic_user = "natas15"
basic_pass = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
