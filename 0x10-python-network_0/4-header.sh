#!/bin/bash
#take URL as arg, send GET request to URL,and display the body of response
curl -sH "X-School-User-Id: 98" "$1"
