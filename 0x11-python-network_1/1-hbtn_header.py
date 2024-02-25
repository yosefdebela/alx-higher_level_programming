#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

def get_x_request_id(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        x_request_id = headers.get("X-Request-id")
        return x_request_id

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")