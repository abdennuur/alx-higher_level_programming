#!/usr/bin/python3
"""take in URL, send request to URL and display the value of
X-Request-Id variable found in the header of response.

Usage: ./1-hbtn_header.py <URL>
"""
import sys

import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
