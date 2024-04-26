#!/usr/bin/python3
"""
takes in URL and sends a request to the URL displays
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    """Sending post request to URL"""
    req = requests.get(url)
    if req.status_code >= (400):
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
