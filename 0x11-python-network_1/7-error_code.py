#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.

Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""

import sys
import requests

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    r = requests.get(url)

    # Check if the status code indicates an error
    if r.status_code >= 400:
        # Print the error code
        print("Error code: {}".format(r.status_code))
    else:
        # Print the body of the response
        print(r.text)

