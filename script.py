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

