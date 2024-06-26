#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with email as value
    value = {"email": email}

    # Send a POST request with the email data to the specified URL
    r = requests.post(url, data=value)

    # Print the body of the response
    print(r.text)
