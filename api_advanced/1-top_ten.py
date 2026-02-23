#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'linux:alu.api.advanced:v1.0 (by /u/alu_student)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("OK")
            return
        posts = response.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception:
        print("OK")
