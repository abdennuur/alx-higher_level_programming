#!/bin/bash
# take URL and display HTTP methods server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
