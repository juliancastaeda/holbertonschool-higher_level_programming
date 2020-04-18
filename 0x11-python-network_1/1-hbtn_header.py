#!/usr/bin/python3
"""
"""
import urllib.request
import sys


def getRequest():
    """
    """
    with urllib.request.urlopen(sys.argv[1]) as res:
        req = res.headers.get('X-Request-Id')
        print(req)

if __name__ == "__main__":
    getRequest()
