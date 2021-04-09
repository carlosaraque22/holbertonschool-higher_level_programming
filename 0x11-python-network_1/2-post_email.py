#!/usr/bin/python3

"""Sends a POST request to the passed URL with the email as a parameter"""

import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("{}".format(the_page.decode()))
