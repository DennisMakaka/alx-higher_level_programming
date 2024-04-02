#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Create a request object for the specified URL
    request = urllib.request.Request(url)

    # Open the URL and handle the response
    with urllib.request.urlopen(request) as response:
        # Extract and print the value of the X-Request-Id header
        print(dict(response.headers).get("X-Request-Id"))
