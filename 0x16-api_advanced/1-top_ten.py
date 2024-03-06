#!/usr/bin/python3

"""
module to print the titles of the first
10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
     a function that queries the Reddit API and returns the number
     of subscribers (not active users, total subscribers) for a
     given subreddit. If an invalid subreddit is given,
     the function should return 0.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    custom_user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=custom_user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
