#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io using the requests library.
"""

import requests

if __name__ == "__main__":
    # Send a GET request to the specified URL
    r = requests.get("https://alx-intranet.hbtn.io/status")

    # Print information about the response
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))  # Print the type of the response body
    print("\t- content: {}".format(r.text))  # Print the response body content

