#!/usr/bin/python3
"""
Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Get GitHub username and password from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Create Basic Authentication object
    auth = HTTPBasicAuth(username, password)

    # Send a GET request to the GitHub API with Basic Authentication
    r = requests.get("https://api.github.com/user", auth=auth)

    # Print the GitHub ID from the response
    print(r.json().get("id"))

