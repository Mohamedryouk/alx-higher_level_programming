#!/usr/bin/python3
"""Script takes URL and Email"""
import sys
import requests

if __name__ == "__main__":
    """Accepting two arguments"""
    url = sys.argv[1]
    email = sys.argv[2]
    print("Your email is:", email)
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
