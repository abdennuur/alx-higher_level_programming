#!/usr/bin/python3
"""Send POST request to given URL with given email.

Usage: ./2-post_email.py <URL> <email>
  - Display the body of response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    dt = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, dt)
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
