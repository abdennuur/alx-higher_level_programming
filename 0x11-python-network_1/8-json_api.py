#!/usr/bin/python3
"""Send POST request to http://0.0.0.0:5000/search_user with given letter.

Usage: ./8-json_api.py <letter>
  - letter is sent as value of variable `q`.
  - If no letter provided, send `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    ltr = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": ltr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
