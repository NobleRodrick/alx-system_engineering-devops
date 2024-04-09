#!/usr/bin/python3
"""module for the reddit api
the reddit api is something special"""

import json
import requests


def var_cnt_words(subreddit, list_of_words, after="", var_cnt=[]):
    """
    Write a recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces
    """

    if after == "":
        var_cnt = [0] * len(list_of_words)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'Nkefor'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(list_of_words)):
                    if list_of_words[i].lower() == word.lower():
                        var_cnt[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(list_of_words)):
                for j in range(i + 1, len(list_of_words)):
                    if list_of_words[i].lower() == list_of_words[j].lower():
                        save.append(j)
                        var_cnt[i] += var_cnt[j]

            for i in range(len(list_of_words)):
                for j in range(i, len(list_of_words)):
                    if (var_cnt[j] > var_cnt[i] or
                            (list_of_words[i] > list_of_words[j] and
                             var_cnt[j] == var_cnt[i])):
                        aux = var_cnt[i]
                        var_cnt[i] = var_cnt[j]
                        var_cnt[j] = aux
                        aux = list_of_words[i]
                        list_of_words[i] = list_of_words[j]
                        list_of_words[j] = aux

            for i in range(len(list_of_words)):
                if (var_cnt[i] > 0) and i not in save:
                    print("{}: {}".format(list_of_words[i].lower(), var_cnt[i]))
        else:
            var_cnt_words(subreddit, list_of_words, after, var_cnt)
