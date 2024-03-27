#!/bin/bash
#send request to URL passed as arg, and display only the status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
