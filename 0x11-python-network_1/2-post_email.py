#!/usr/bin/python3
"""
Module to send a POST request with an email to a specified URL.
Uses only urllib and sys packages.
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    emailData = {"email": sys.argv[2]}
    pasring = urllib.parse.urlencode(emailData).encode("ascii")

    request = urllib.request.Request(url, pasring)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
