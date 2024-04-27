#!/usr/bin/python3
"""
Fetching a URL using the requests package.
"""

import requests


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    url = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: <class '{}'>".format(url.text.__class__))
    print("\t- content: {}".format(url.text))
