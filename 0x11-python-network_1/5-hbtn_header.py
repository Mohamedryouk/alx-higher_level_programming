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
    
    url = sys.argv[1]
    try:
        req = requests.get(url)
        print(req.headers.get("X-Request-Id"))
    except Exception as e:
        pass
