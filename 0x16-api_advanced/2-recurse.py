#!/usr/bin/python3

"""
Module Documentation
"""

import requests


def recurse(subreddit, hot_list=None, count=0, after=None):
    """
    Function Documentation
    """
    if hot_list is None:
        hot_list = []

    url = 'https://www.reddit.com'
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    if after is None:
        after = ''

    response = requests.get(
        '{}/r/{}/.json?sort={}&limit={}&count={}&after={}'.format(
            url, subreddit, 'hot', 30, count, after),
        headers=headers,
        allow_redirects=False
    )

    if response.status_code == 200:
        posts = response.json()['data']['children']
        hot_list.extend(map(lambda x: x['data']['title'], posts))

        if len(posts) >= 30 and response.json()['data']['after']:
            return recurse(subreddit, hot_list, count + len(posts),
                           response.json()['data']['after'])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
