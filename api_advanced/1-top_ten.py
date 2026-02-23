#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints titles of first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'linux:alu.api.advanced:v1.0 (by /u/alu_student)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            # non-existent subreddit or forbidden
            print("OK")
            return
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    except Exception:
        # network error or JSON parsing error
        print("OK")
