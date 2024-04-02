#!/bin/bash
# send a request to a URL and displays only te status code of te response
curl -s -o /dev/null -w "%{http_code}" "$1"
