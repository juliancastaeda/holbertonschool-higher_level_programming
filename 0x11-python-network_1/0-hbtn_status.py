#!/usr/bin/python3
"""
"""
import urllib.request


def getStatus():
    """
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        cont = res.read()
        type_cont = type(cont)
        print("Body response:")
        print("\t- type: {}".format(type_cont))
        print("\t- cont: {}".format(cont))
        print("\t- utf8 cont: {}".format(cont.decode('utf-8')))

if __name__ == "__main__":
    getStatus()
