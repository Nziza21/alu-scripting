#!/usr/bin/python3
"""Function that queries Reddit API and prints top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:my.reddit.app:v1.0 (by /u/test)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data", {}).get("children", [])
    for post in data:
        print(post.get("data", {}).get("title"))
