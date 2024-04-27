#!/usr/bin/python3
"""
Printing the HTTPError code
"""
import urllib
import sys
from urllib.error import URLError, HTTPError
import urllib.request


if __name__ == "__main__":
    """
    main: name
    """
    url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode("UTF-8")
        print(body)
except HTTPError as e:
    print(f"Error code: {e.code}")
except URLError as er:
    print(f"Connection error: {er.reason}")
