#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        hot_list (list): List to store titles of hot articles.
        after (str): Identifier for the starting point of the search.

    Returns:
        list: List containing the titles of hot articles.
               If no results are found, returns None.
    """
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 100, 'after': after}
    response = requests.get(
        base_url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child.get('data', {}).get('title', '')
            hot_list.append(title)

        after = data.get('after', None)

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    elif response.status_code == 404:
        print("Subreddit not found.")
        return None
    else:
        print("Error:", response.status_code)
        return None

# For later testing
# if __name__ == "__main__":
#     result = recurse(sys.argv[1])
#     if result is not None:
#         print(len(result))
#     else:
#         print("None")
