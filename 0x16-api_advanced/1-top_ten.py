#!/usr/bin/python3
"""uses reddit API to check for hottest post of a subreddit"""
import requests


def top_ten(subreddit):
    """function that queries the reddit API"""
    url = 'http://reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'fullstack_posthunter'}
    page = requests.get(url, headers=headers).json()
    try:
        children = page.get('data', None).get('children')
        if children:
            for child in children:
                print(child.get('data', None).get('title', None))
    except Exception:
        print(None)
