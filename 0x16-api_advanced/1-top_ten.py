#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit"""

    import requests
    sub_data = requests.get("https://www.reddit.com/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agenet": "My-User-Agent"},
                            allow_redirects=False)
    if sub_data >= 300:
        print('None')
    else:
        for child in sub_info.json().get("data").get("children"):
            print(child.get(data).get(title))
