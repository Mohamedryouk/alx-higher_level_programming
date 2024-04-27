#!/usr/bin/python3
"""
Module to send a POST request with an email to a specified URL.
Uses only urllib and sys packages.
"""
import sys
import urllib.request
import urllib.parse


def postEmail(url, email):
    """
        Sends a POST request to the specified URL with the given email.

        Args:
            url (str): The URL to send the POST request to.
            email (str): The email to be sent in the POST request.

        Returns:
            None

        Raises:
            Exception: If an error occurs during the POST request.
        """
    url = sys.argv[1]
    email = sys.argv[2]
    print("Your email is:", email)
    emailBytes = email.encode('utf-8')
    try:
        # Send a POST request to the url and email passed
        with urllib.request.urlopen(url, data=emailBytes) as response:
            # Read the response and print it to the user
            body = response.read().decode('utf-8')
            print("Response body:", body)
    except Exception as e:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <enmil>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    postEmail(url, email)
