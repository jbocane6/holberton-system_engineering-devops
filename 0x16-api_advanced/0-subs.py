#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
Hint: No authentication is necessary for most features of the Reddit API.
    If you’re getting errors related to Too Many Requests,
    ensure you’re setting a custom User-Agent.
Requirements:
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    note: Invalid subreddits may return a redirect to search results.
        Ensure that you are not following redirects.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
        for a given subreddit.
    """
    user_agent_str = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0)'
                      'Gecko/20190101 Firefox/77.0')
    user_ag = {'User-Agent': user_agent_str}
    session = requests.Session()
    session.headers.update(user_ag)

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    request = session.get(url, headers=user_ag)
    if (request.status_code == 404):
        return 0

    return request.json().get('data').get('subscribers')
