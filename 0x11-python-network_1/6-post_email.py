#!/usr/bin/python3
"""To take in URL and email address, send POST request to the passed
URL with email as a parameter, and display the body of response
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    print(req.text)
