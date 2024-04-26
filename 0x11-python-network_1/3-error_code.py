#!/usr/bin/python3
# A script that takes in a URL and sends a request to the URL
# and displays the body of the response
 
import urllib
import sys
from urllib.error import URLError,HTTPError
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode("UTF-8")
        print(body)
except HTTPError as e:
    print(f"Error code: {e.code}")
except URLError as er:
    print(f"Connection error: {er.reason}")
