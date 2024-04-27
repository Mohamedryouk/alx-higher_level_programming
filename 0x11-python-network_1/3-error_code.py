#!/usr/bin/python3
"""
Module for printing HTTPError code or connection error reason.
"""

import sys
import urllib.request
from urllib.error import URLError, HTTPError


def main(url):
    """
    Main function to print the content of the URL or handle errors.

    Args:
        url (str): The URL to fetch content from.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("UTF-8")
            print(body)
    except HTTPError as e:
        print(f"Error code: {e.code}")
    except URLError as er:
        print(f"Connection error: {er.reason}")


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    main(url)
