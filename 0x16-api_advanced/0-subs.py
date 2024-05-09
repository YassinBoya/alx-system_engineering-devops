#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """ a function thatQueries the Reddit API and returns the number
    of subscribersto the subreddit"""
    import requests

    sub_data = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_data.status_code >= 300:
        return 0

    return sub_data.json().get("data").get("subscribers")
