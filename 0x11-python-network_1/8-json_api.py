#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""

import sys
import requests

if __name__ == "__main__":
    # Get the letter from command line arguments or set it to empty string if not provided
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Create payload dictionary with the letter
    payload = {"q": letter}

    # Send a POST request with the payload to the specified URL
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Parse the response as JSON
        response = r.json()
        if response == {}:
            # Print message if no result is returned
            print("No result")
        else:
            # Print the id and name from the response
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        # Handle case where response is not valid JSON
        print("Not a valid JSON")

