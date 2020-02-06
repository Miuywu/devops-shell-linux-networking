#!/usr/bin/python3
""" retrieves number of subscribers of subreddit """
import requests


def number_of_subscribers(subreddit):
    rURL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {"User-Agent": 'any agent'}

    data = requests.get(rURL, headers=h, allow_redirects=False).json()
    if data is None:
        return 0
    data2 = data.get('data')
    return data2.get('subscribers')