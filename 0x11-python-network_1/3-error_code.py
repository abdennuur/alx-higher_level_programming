#!/usr/bin/python3
"""
takes in URL, send a request to URL and display
the body of response "decoded in utf-8".
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as resp:
            print(resp.read().decode("ascii"))
    except error.HTTPError as er:
        print("Error code: {}".format(er.code))
