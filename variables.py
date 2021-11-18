"""Project variables
"""

# Third party import
from requests.auth import HTTPBasicAuth

BASIC_USER = "natas15"
BASIC_PASS = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
NAME = 'natas16'
STOP_TIME = 0.01

auth = HTTPBasicAuth(BASIC_USER, BASIC_PASS)
URL = "http://natas15.natas.labs.overthewire.org/index.php"
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
