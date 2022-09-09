# CMPUT 404 Lab 1
# CCID: kli1
# Author: Ke Li

import requests

# prints out the version of the requests library

print(requests.__version__)


# GET the Google homepage
# cite: https://www.w3schools.com/Python/ref_requests_get.asp

url = "http://google.com/"
s = requests.get(url)
print(s)


# Downloads itself from GitHub and prints out its own source code from GitHub.

url = "https://raw.githubusercontent.com/kkli08/CMPUT404/main/script.py"
sourcecode = requests.get(url)
print(sourcecode.text)

