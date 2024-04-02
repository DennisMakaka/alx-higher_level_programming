#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""

import sys
import requests

if __name__ == "__main__":
    # Construct the URL for the GitHub API
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send a GET request to the GitHub API
    r = requests.get(url)

    # Parse the response as JSON
    commits = r.json()

    try:
        # Iterate over the first 10 commits
        for i in range(10):
            # Print the commit hash and author name
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        # Handle case where there are fewer than 10 commits
        pass

