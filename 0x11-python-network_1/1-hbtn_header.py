#!/usr/bin/python3
# Script that takes in a URL and sends
# a request to the URL and displays the values

import urllib.request
import sys

if len(sys.argv) < 2:
    sys.exit(1)
# Accepting a URL
url = sys.argv[1]
# Try sending a request to the added URL
try:
    with urllib.request.urlopen(url) as response:
        # getting the request id and stor
        # it in request_id and formating it using print.
        request_id = response.headers.get("X-Request-Id")
        print("{}".format(request_id))
except Exception as e:
    # exception handler for URL Errors.
    print("Error:", e)
