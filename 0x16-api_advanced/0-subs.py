#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given,
the function should return 0.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    custom_user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=custom_user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
