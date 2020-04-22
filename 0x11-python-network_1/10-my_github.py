#!/usr/bin/python3
""" 
"""

import requests
import sys

if __name__ == "__main__":
    """
    """
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    json = requests.get(url, auth=(user, password)).json()
    try:
        print(json["id"])
    except:
        print(None)
