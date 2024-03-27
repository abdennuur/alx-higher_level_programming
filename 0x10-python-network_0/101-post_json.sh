#!/bin/bash
# Send JSON POST request to  URL with JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
