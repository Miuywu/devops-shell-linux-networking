#!/usr/bin/python3
""" recursively saves all hot posts of a subreddit into a list """
import requests


def recurse(subreddit, hot_list=[]):
    rURL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    h = {"User-Agent": 'any agent'}
    derulo = requests.get(rURL, headers=h, allow_redirects=False).json()
    if derulo is None:
        return
    data = derulo.get('data')
    if data is None:
        return
    post_list = data.get('children')
    return(post_list)
