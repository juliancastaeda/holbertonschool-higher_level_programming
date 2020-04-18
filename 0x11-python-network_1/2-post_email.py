#!/usr/bin/python3
"""
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    """
    """
    url = argv[1]
    value = {'email': argv[2]}

    data = urlencode(value)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        content = res.read().decode('utf-8')
        print(content)
