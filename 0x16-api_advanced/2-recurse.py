#!/usr/bin/python3
"""
This module uses reddit API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None"""
    global after
    custom_user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=custom_user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        converted_data = results.json().get("data").get("after")
        if converted_data is not None:
            after = converted_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
