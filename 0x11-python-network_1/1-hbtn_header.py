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
    Main entry point of the script.
    """
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    # Accepting a URL
    url = sys.argv[1]

    # Try sending a request to the provided URL
    try:
        with urllib.request.urlopen(url) as response:
            # Getting the request id from the response headers
            request_id = response.headers.get("X-Request-Id")
            print("Request ID:", request_id)
    except Exception as e:
        # Exception handler for URL errors
        print("Error:", e)
