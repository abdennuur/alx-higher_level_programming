#!/bin/bash
#take in URL, send a request to URL,and display the size of body of response
curl -s "$1" | wc -c
