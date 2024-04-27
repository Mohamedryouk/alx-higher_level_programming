#!/usr/bin/python3
"""
Using requestes package to send a request
"""

import sys
import requests


if __name__ == "__main__":
    """
    main entry to get URL
    """
    if len(sys.argv) < 2:
        sys.exit(1)
    url = sys.argv[1]
    try:
        with requests.post(url) as response:
            req_id = response.headers.get("X-Request-Id")
            print("{}".format(req_id))
    except Exception as e:
        pass
