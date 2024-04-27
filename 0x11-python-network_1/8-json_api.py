#!/usr/bin/python3
"""
    main: name
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    # posting the request to the url
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        response_json = response.json()
        if response_json:
            res = response_json.get('name')
            print("[{}] {}".format(response_json.get('id'), res))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
