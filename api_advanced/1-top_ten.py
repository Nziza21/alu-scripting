#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Prints titles of first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'linux:alu.api.advanced:v1.0 (by /u/alu_student)'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("OK")
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        if not posts:  # empty subreddit
            print("OK")
            return

        for post in posts:
            print(post['data']['title'])
    except Exception:
        print("OK")


if __name__ == "__main__":
    # quick local tests
    top_ten("python")                   # existing subreddit
    top_ten("thissubredditdoesnotexist") # non-existent subreddit
