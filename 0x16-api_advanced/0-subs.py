#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {'User-Agent': 'My-User-Agent'}
    sub_info = requests.get(url, headers=headers, allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0
    sub_info = sub_info.json()
    if 'data' in sub_info:
        return sub_info.get("data").get("subscribers")
    else:
        return 0
