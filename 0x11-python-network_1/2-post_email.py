#!/usr/bin/python3
#Taking URL and an email and send a POST request to the passed URL and email
import sys
import urllib.request
import urllib.parse
def postEmail(url, email):
    url = sys.argv[1]
    email = sys.argv[2]
    print("Your email is:", email)
    emailBytes = email.encode('utf-8')
    try:
        # Send a POST request to the url and email passed
        with urllib.request.urlopen(url, data=emailBytes) as response:
            # Read the response and print it to the user
            body = response.read().decode('utf-8')
            print("Response body:",body)
    except Exception as e:
        pass
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <enmil>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    postEmail(url, email)