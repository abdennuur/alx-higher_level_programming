#!/usr/bin/python3
"""List 10 most recent commits on given GitHub repo.

Usage: ./100-github_commits.py <repo name> <repo owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for ix in range(10):
            print("{}: {}".format(
                commits[ix].get("sha"),
                commits[ix].get("commit").get("author").get("name")))
    except IndexError:
        pass
