#!/bin/bash
# send DELETE request to URL passed as first argg and display the body of response
curl -sX DELETE "$1"
