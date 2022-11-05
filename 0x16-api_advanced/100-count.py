#!/usr/bin/python3
"""Module API """

import re
import requests


def sort_dict(word_dict):
    """sorts the dictionary based on keys"""
    word_keys = word_dict.keys()
    word_values = word_dict.values()
    word_items = sorted(zip(word_values, word_keys), reverse=True)
    for value, word in word_items:
        print('{}: {}'.format(word, value))


def count_words(subreddit, word_list, after=None, words_count={}):
    """function that queries the Reddit API and prints a dictionary
    containing the count of words in word_list in all hot articles
    for a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"

    if after:
        url = url.format(subreddit, after)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    header = {"User-Agent": "recursing_dev"}

    request = requests.get(url, headers=header)

    if request.status_code != 200:
        return None

    if request.status_code == 200:
        children = request.json().get("data").get("children")
        after = request.json().get("data").get("after")

        if children is None:
            return None

        for child in children:
            titles = child.get("data").get("title")
            for word in word_list:
                regex = r'\b{}\b'.format(word)
                word_find = re.findall(regex, titles, re.I)
                if word_find:
                    word = word.lower()
                    num_words = len(word_find)
                    words_count[word] = words_count.get(word, 0) + num_words

    if after:
        count_words(subreddit, word_list, after=after, words_count=words_count)
    else:
        sort_dict(words_count)

    return words_count
