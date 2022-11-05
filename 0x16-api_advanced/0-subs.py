#!/usr/bin/python3
"""uses reddit API to check for total subcribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the reddit API"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'fullstack'}
    page = requests.get(url, headers=headers, allow_redirects=False).json()
    try:
        return page.get('data', 0).get('subscribers', 0)
    except Exception:
        return 0
