#!/usr/bin/python3
"""
Request the X-Request-Id from a given URL.

This script takes a URL as a command-line argument and sends a request to it.
It then extracts the X-Request-Id header from the response and prints it.

Usage:
    ./script_name.py <URL>

Example:
    ./script_name.py https://example.com
"""


import urllib.request
import sys


if __name__ == "__main__":
    """
    main - name
    """
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
