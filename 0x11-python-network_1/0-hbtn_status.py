#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io.
"""

import urllib.request

if __name__ == "__main__":
    # Create a request object for the specified URL
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    # Open the URL and handle the response
    with urllib.request.urlopen(request) as response:
        # Read the response body
        body = response.read()

        # Print information about the response
        print("Body response:")
        print("\t- type: {}".format(type(body)))  # Print the type of the response body
        print("\t- content: {}".format(body))  # Print the response body content
        print("\t- utf8 content: {}".format(body.decode("utf-8")))  # Print the response body content in utf-8 format.
