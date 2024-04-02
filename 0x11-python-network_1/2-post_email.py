#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode email data
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create a POST request with the encoded data
    request = urllib.request.Request(url, data=data)

    # Send the request and handle the response
    with urllib.request.urlopen(request) as response:
        # Print the body of the response
        print(response.read().decode("utf-8"))
