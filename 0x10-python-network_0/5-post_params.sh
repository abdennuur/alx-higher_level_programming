#!/bin/bash
#take URL, send POST request to passed URL, and display the body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
