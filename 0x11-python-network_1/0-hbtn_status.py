#!/usr/bin/python3
#Fetching a URL using urllib package.

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()

    body_str = body.decode('utf-8')
    content_type = type(body).__name__
    print("Body response:")
    print("\t- type: <class '{}'>".format(content_type))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body_str))
