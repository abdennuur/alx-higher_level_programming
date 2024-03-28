#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        resp = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode(encoding='utf-8')))
