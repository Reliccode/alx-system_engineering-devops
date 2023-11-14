#!/usr/bin/python3
"""
Queries the Reddit API and retrieves the titles of the top hot posts.
"""

import requests


def extract_titles(hot_posts):
    """Extract titles from a list of posts."""
    return [post['data']['title'] for post in hot_posts]


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve titles of hot posts.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list, optional): List to store titles.
        after (str, optional): Parameter for pagination.

    Returns:
        list or None: List of titles if successful, None if there's an issue.
    """
    if hot_list is None:
        hot_list = []

    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    params = {'after': after} if after else {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data from Reddit API. Status Code:
              {response.status_code}")
        return None

    data = response.json().get('data', {})
    hot_posts = data.get('children', [])

    hot_list.extend(extract_titles(hot_posts))

    after = data.get('after')
    if not after:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)


# Example usage:
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
