#!/usr/bin/python3
"""
 take in URL, send request to URL and display the value
 of variable X-Request-Id in response header
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
