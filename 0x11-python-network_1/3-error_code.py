#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    # Get the URL from command line arguments
    url = sys.argv[1]

    # Create a request object for the specified URL
    request = urllib.request.Request(url)

    try:
        # Open the URL and handle the response
        with urllib.request.urlopen(request) as response:
            # Print the body of the response
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the error code
        print("Error code: {}".format(e.code))
