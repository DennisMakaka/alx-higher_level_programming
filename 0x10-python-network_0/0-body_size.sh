#!/bin/bash
# This script takes a URL, sends a request, and displays the size of the response body in bytes

# Send a request to the URL and get the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

