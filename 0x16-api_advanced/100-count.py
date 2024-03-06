#!/usr/bin/python3
""" module for the reddit api
raddit api"""

import json
import requests


def count_variable_words(subreddit, word_list, after="", count_variable=[]):
    """will go through the entire api and count_variable occurences
    htranks
    """

    if after == "":
        count_variable = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count_variable[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count_variable[i] += count_variable[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count_variable[j] > count_variable[i] or
                            (word_list[i] > word_list[j] and
                             count_variable[j] == count_variable[i])):
                        aux = count_variable[i]
                        count_variable[i] = count_variable[j]
                        count_variable[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count_variable[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count_variable[i]))
        else:
            count_variable_words(subreddit, word_list, after, count_variable)
