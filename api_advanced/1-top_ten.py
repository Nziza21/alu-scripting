#!/usr/bin/python3
"""Module that queries the Reddit API and prints the top 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "alu-scripting-project/1.0"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            print(None)
            return

        posts = res.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
